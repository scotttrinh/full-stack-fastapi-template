import logging
import uuid

import fastapi
import gel.auth
import gel.fastapi
import sentry_sdk
from fastapi.routing import APIRoute

from app.core.config import settings
from app.frontend import frontend_router

logging.basicConfig(level=logging.INFO)
logging.getLogger("gel.auth").setLevel(logging.DEBUG)


def custom_generate_unique_id(route: APIRoute) -> str:
    if route.tags:
        return f"{route.tags[0]}-{route.name}"
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


@g.auth.on_new_identity
async def on_new_identity(
    result: tuple[uuid.UUID, gel.auth.TokenData | None],
    client: gel.fastapi.Client,
    request: fastapi.Request,
) -> fastapi.Response | None:
    json = await request.json()
    full_name = json.get("full_name")

    await client.query_required_single(
        """
        with
          IDENTITY := <ext::auth::Identity><uuid>$identity_id
        insert User {
          identity := IDENTITY,
          email := (select ext::auth::EmailPasswordFactor filter .identity = IDENTITY).email,
          full_name := <optional str>$full_name,
        }
        """,
        identity_id=result[0],
        full_name=full_name,
    )


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)


from app.api.main import api_router  # noqa: E402, I001

app.include_router(api_router, prefix=settings.API_V1_STR)

app.include_router(frontend_router)
