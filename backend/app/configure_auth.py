import gel
import gel.fastapi

from app.core.config import settings


def configure_branch_auth() -> None:
    """Configure branch authentication.

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
configure current branch reset cfg::SMTPProviderConfig;
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

# Configure email provider to use Mailpit Sandbox
configure current branch insert cfg::SMTPProviderConfig {{
  name := "mailtrap_sandbox",
  sender := "hello@example.com",
  host := "sandbox.smtp.mailtrap.io",
  port := <int32>2525,
  username := "{{config.MAILTRAP_USER}}",
  password := "{{config.MAILTRAP_PASSWORD}}",
  timeout_per_email := <duration>"PT5M",
  timeout_per_attempt := <duration>"PT1M",
  validate_certs := false,
}};
configure current branch set cfg::current_email_provider_name := "mailtrap_sandbox";
        """
    )


if __name__ == "__main__":
    configure_branch_auth()
