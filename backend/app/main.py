import os

import sentry_sdk
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles

from app.api.main import api_router
from app.core.config import settings


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

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
async def frontend_router_redirect(_: str):
    return FileResponse(index_path)
