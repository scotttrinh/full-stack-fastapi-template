import uuid
from collections.abc import Callable, Generator
from dataclasses import dataclass
from typing import Any

import gel.fastapi
import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app
from app.models.data import Item, User


@dataclass
class TestUser:
    """A test user with authentication details and convenience methods."""

    email: str
    password: str
    full_name: str
    id: uuid.UUID
    is_superuser: bool
    client: TestClient
    auth_token: str
    _db_client: gel.Client
    _impersonate_user: Callable[[str], gel.Client]

    @property
    def db(self) -> gel.Client:
        """Get an impersonated database client for this user."""
        return self._impersonate_user(str(self.id))

    @property
    def request(self) -> TestClient:
        """Get an authenticated test client for this user."""
        self.client.headers = self._get_headers()
        return self.client

    def _get_headers(self) -> dict[str, str]:
        """Get authentication headers for this user with valid cookie attributes."""
        cookie_value = f"gel_auth_token={self.auth_token}; Path=/; HttpOnly"
        return {
            "cookie": cookie_value,
        }


@dataclass
class TestUsers:
    """Container for all test users with convenience methods."""

    superuser1: TestUser
    superuser2: TestUser
    user1: TestUser
    user2: TestUser

    def get_user(self, user_type: str) -> TestUser:
        """Get a user by type: 'superuser1', 'superuser2', 'user1', 'user2'."""
        return getattr(self, user_type)

    def as_user(self, user_type: str):
        """Get a context manager-like interface for a specific user."""
        return self.get_user(user_type)


@pytest.fixture(scope="session")
def db() -> Generator[gel.Client, None, None]:
    client = gel.create_client()
    yield client
    client.query(Item.delete())
    client.query(User.delete())


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def impersonate_user(db: gel.Client) -> Callable[[str], gel.Client]:
    def _impersonate_user(user_id: str) -> gel.Client:
        return db.with_globals({"spoof_user_id": user_id})

    return _impersonate_user


@pytest.fixture(scope="session")
def allaccess_client(db: gel.Client) -> gel.Client:
    return db.with_config({"apply_access_policies": False})  # type: ignore


# Branch authentication configuration is now handled by the configure_auth.py script
# which is called from test.sh before running pytest


@pytest.fixture(scope="session")
def test_users(
    db: gel.Client,
    allaccess_client: gel.Client,
    impersonate_user: Callable[[str], gel.Client],
) -> TestUsers:
    """Create test users for impersonation testing."""

    def create_user(
        email: str, password: str, full_name: str, is_superuser: bool = False
    ) -> TestUser:
        # Create a new client instance for this user
        user_client = TestClient(app)

        # Register the user
        register_r = user_client.post(
            "/auth/register",
            data={
                "email": email,
                "password": password,
            },
        )
        register_r.raise_for_status()

        register_response = register_r.json()
        auth_token = register_response["access_token"]
        identity_id = register_response["identity_id"]

        user_id: uuid.UUID = allaccess_client.query_required_single(
            """
            with
              USER := assert_exists(
                (<ext::auth::Identity><uuid>$identity_id.<[identity is User]),
                "User not found for identity"
              )
            select USER.id;
            """,
            identity_id=identity_id,
        )

        if is_superuser:
            allaccess_client.query(
                """
                with
                  USER := assert_exists(
                    (<ext::auth::Identity><uuid>$identity_id.<[identity is User]),
                    "User not found for identity"
                  )
                update USER set { is_superuser := true };
                """,
                identity_id=identity_id,
            )

        return TestUser(
            email=email,
            password=password,
            full_name=full_name,
            id=user_id,
            is_superuser=is_superuser,
            client=user_client,
            auth_token=auth_token,
            _db_client=db,
            _impersonate_user=impersonate_user,
        )

    # Create test users
    superuser1 = create_user(
        email="superuser1@example.com",
        password="superuser1password",
        full_name="Super User 1",
        is_superuser=True,
    )

    superuser2 = create_user(
        email="superuser2@example.com",
        password="superuser2password",
        full_name="Super User 2",
        is_superuser=True,
    )

    user1 = create_user(
        email="user1@example.com",
        password="user1password",
        full_name="Regular User 1",
        is_superuser=False,
    )

    user2 = create_user(
        email="user2@example.com",
        password="user2password",
        full_name="Regular User 2",
        is_superuser=False,
    )

    return TestUsers(
        superuser1=superuser1,
        superuser2=superuser2,
        user1=user1,
        user2=user2,
    )
