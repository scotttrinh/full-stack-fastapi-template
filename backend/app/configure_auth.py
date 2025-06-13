import gel
import gel.fastapi

from app.core.config import settings


def configure_branch_auth() -> str:
    """Configure branch authentication and return the signing key.

When you run this script, it will reset all auth-related configuration to default,
and cause existing auth tokens to be invalidated (new random signing key).

You can set the GEL_AUTH_SIGNING_KEY environment variable to a specific value to
use that signing key instead of generating a new one.
"""

    db = gel.create_client()

    db.execute(
        f"""
# Reset all auth configs to their defaults
configure current branch reset cfg::cors_allow_origins;
configure current branch reset cfg::EmailProvider;
configure current branch reset cfg::current_email_provider_name;
configure current branch reset ext::auth::EmailPasswordProviderConfig;
configure current branch reset ext::auth::ProviderConfig;
configure current branch reset ext::auth::AuthConfig;

# Configure core auth settings
configure current branch set ext::auth::AuthConfig::app_name := "{settings.PROJECT_NAME}";
configure current branch set ext::auth::AuthConfig::auth_signing_key := "{settings.GEL_AUTH_SIGNING_KEY}";
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

# Configure email and password auth provider
configure current branch insert ext::auth::EmailPasswordProviderConfig {{
  require_verification := false
}};

# Configure email provider to use Mailpit
configure current branch insert cfg::EmailProvider {{
  name := "Mailpit",
  sender := "noreply@example.com",
  host := "localhost",
  port := 1025,
  validate_certs := false,
}};
configure current branch set cfg::current_email_provider_name := "Mailpit";
        """
    )

    return signing_key


if __name__ == "__main__":
    signing_key = configure_branch_auth()
    print(f"Branch authentication configured with signing key: {signing_key}")
