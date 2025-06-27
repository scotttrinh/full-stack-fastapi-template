import logging
import typing
import uuid

import fastapi
import gel.auth
import gel.fastapi
import gel.fastapi.auth.email_password as ep
import sentry_sdk
from fastapi.routing import APIRoute
from pydantic import BaseModel

from app.core.config import settings
from app.frontend import frontend_router

logging.basicConfig(level=logging.INFO)
logging.getLogger("gel.auth").setLevel(logging.DEBUG)


def custom_generate_unique_id(route: APIRoute) -> str:
    if route.tags:
        return f"{route.tags[0]}/{route.name}"
    return route.name


app = fastapi.FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

g = gel.fastapi.gelify(app)


@app.get("/error")
def error_page(error: str):
    return error


class CreateUser(ep.SignUpBody):
    full_name: str | None = None


@g.auth.email_password.on_sign_up_complete
async def on_sign_up_complete(
    result: gel.auth.email_password.SignUpCompleteResponse,
    client: gel.fastapi.Client,
    request: fastapi.Request,
):
    user = CreateUser.model_validate(await request.json())
    await client.query_required_single(
        """
        with
          IDENTITY := <ext::auth::Identity><uuid>$identity_id,
        insert User {
          identity := IDENTITY,
          email := (select ext::auth::EmailPasswordFactor filter .identity = IDENTITY).email,
          full_name := <optional str>$full_name,
        }
        """,
        identity_id=result.identity_id,
        full_name=user.full_name,
    )


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)


from app.api.main import api_router  # noqa: E402, I001

app.include_router(api_router, prefix=settings.API_V1_STR)

app.include_router(frontend_router)
