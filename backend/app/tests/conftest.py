import uuid
from collections.abc import Callable, Generator

import gel.fastapi
import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app
from app.models.data import Item, User


@pytest.fixture(scope="session")
def db() -> Generator[gel.Client, None, None]:
    client = gel.create_client()
    yield client
    client.query(Item.delete())
    client.query(User.delete())


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def impersonate_user(db: gel.Client) -> Callable[[str], gel.Client]:
    def _impersonate_user(user_id: str) -> gel.Client:
        return db.with_globals({"spoof_user_id": user_id})

    return _impersonate_user


@pytest.fixture(scope="module")
def allaccess_client(db: gel.Client) -> gel.Client:
    return db.with_config({"apply_access_policies": False})


@pytest.fixture(scope="session", autouse=True)
def configure_branch_auth(db: gel.Client) -> str:
    signing_key = str(uuid.uuid4())
    db.execute(
        f"""
# Reset all auth configs to their defaults
configure current branch reset cfg::cors_allow_origins;
configure current branch reset ext::auth::EmailPasswordProviderConfig;
configure current branch reset ext::auth::ProviderConfig;
configure current branch reset ext::auth::AuthConfig;

configure current branch set ext::auth::AuthConfig::app_name := "{settings.PROJECT_NAME}";
configure current branch set ext::auth::AuthConfig::auth_signing_key := "{signing_key}";
configure current branch set ext::auth::AuthConfig::allowed_redirect_urls := {{
  "http://localhost:8000",
}};

configure current branch set cfg::cors_allow_origins := {{
  "http://localhost:8000",
}};

configure current database insert ext::auth::EmailPasswordProviderConfig {{
  require_verification := false
}};
        """
    )

    return signing_key
