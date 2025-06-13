import uuid

import gel
import gel.fastapi

from app.core.config import settings


def configure_branch_auth() -> str:
    """Configure branch authentication and return the signing key."""
    db = gel.create_client()
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
  "http://127.0.0.1:8000",
  "http://localhost:8000",
  "http://testserver",
}};

configure current branch set cfg::cors_allow_origins := {{
  "http://127.0.0.1:8000",
  "http://localhost:8000",
  "http://testserver",
}};

configure current database insert ext::auth::EmailPasswordProviderConfig {{
  require_verification := false
}};
        """
    )

    return signing_key


if __name__ == "__main__":
    signing_key = configure_branch_auth()
    print(f"Branch authentication configured with signing key: {signing_key}")
