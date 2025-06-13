import logging
import os
import uuid

import fastapi
import gel.auth
import gel.fastapi
import sentry_sdk
from fastapi.responses import FileResponse
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles

from app.api.main import api_router
from app.core.config import settings

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

gel_auth = gel.fastapi.gelify(app).auth


@app.get("/error")
def error_page(error: str):
    return error


@gel_auth.on_new_identity
async def on_new_identity(
    result: tuple[uuid.UUID, gel.auth.TokenData | None], client: gel.fastapi.Client
) -> fastapi.Response | None:
    await client.query_required_single(
        """
        with
          IDENTITY := <ext::auth::Identity><uuid>$identity_id
        insert User {
          identity := IDENTITY,
          email := IDENTITY.<[identity is ext::auth::EmailFactor].email,
        }
        """,
        identity_id=result[0],
    )


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app.include_router(api_router, prefix=settings.API_V1_STR)

# Serve the React frontend application directly from your FastAPI server

current_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dist_path = os.path.join(current_dir, "..", "..", "frontend", "dist")
static_files_path = os.path.normpath(frontend_dist_path)
index_path = os.path.join(static_files_path, "index.html")

app.mount(
    "/",
    StaticFiles(
        directory=static_files_path,
        html=True,
        check_dir=True,
    ),
    name="frontend",
)


@app.get("/{full_path:path}", include_in_schema=False)
async def frontend_router_redirect():
    return FileResponse(index_path)
