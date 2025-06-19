import uuid
from collections.abc import Generator
from dataclasses import dataclass

import gel.fastapi
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.data import Item, User


@dataclass
class TestUser:
    """A test user with authentication details and convenience methods."""

    __test__ = False
    email: str
    password: str
    full_name: str
    id: uuid.UUID
    is_superuser: bool
    client: TestClient
    auth_token: str
    db: gel.Client

    @property
    def request(self) -> TestClient:
        """Get an authenticated test client for this user."""
        self.client.headers = self._get_headers()
        return self.client

    @property
    def cookies(self) -> dict[str, str]:
        return {
            "gel_auth_token": self.auth_token,
        }

    def _get_headers(self) -> dict[str, str]:
        """Get authentication headers for this user with valid cookie attributes."""
        cookie_value = f"gel_auth_token={self.auth_token}; Path=/; HttpOnly"
        return {
            "cookie": cookie_value,
        }


@dataclass
class TestUsers:
    """Container for all test users with convenience methods."""

    __test__ = False
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
    with TestClient(app, follow_redirects=False) as c:
        yield c


@pytest.fixture(scope="session")
def allaccess_client(db: gel.Client) -> gel.Client:
    return db.with_config({"apply_access_policies": False})  # type: ignore


# Branch authentication configuration is now handled by the configure_auth.py script
# which is called from test.sh before running pytest


@pytest.fixture(scope="session")
def test_users(
    db: gel.Client,
    allaccess_client: gel.Client,
    client: TestClient,
) -> TestUsers:
    """Create test users for impersonation testing."""

    def create_user(
        email: str,
        password: str,
        full_name: str,
        is_superuser: bool = False,
    ) -> TestUser:
        # Register the user
        register_r = client.post(
            "/auth/register",
            json={
                "email": email,
                "password": password,
                "full_name": full_name,
            },
        )

        assert register_r.status_code == 303

        auth_token = register_r.cookies.pop("gel_auth_token")
        nonlocal db
        db = db.with_globals({"ext::auth::client_token": auth_token})

        user = db.query_required_single("select (global current_user) {*}")
        assert user.email == email
        assert user.full_name == full_name

        if is_superuser:
            allaccess_client.query_required_single(
                """
                with
                  USER := <User><uuid>$user_id
                update USER set { is_superuser := true };
                """,
                user_id=user.id,
            )

        return TestUser(
            email=email,
            password=password,
            full_name=full_name,
            id=user.id,
            is_superuser=is_superuser,
            client=client,
            auth_token=auth_token,
            db=db,
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
