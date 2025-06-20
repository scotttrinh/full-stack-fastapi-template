import contextlib
import logging
import os

import fastapi
import httpx
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.core.config import settings


@contextlib.asynccontextmanager
async def frontend_lifespan(app: fastapi.FastAPI):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    frontend_dist_path = os.path.join(current_dir, "..", "..", "frontend", "dist")
    static_files_path = os.path.normpath(frontend_dist_path)
    index_path = os.path.join(static_files_path, "index.html")

    _frontend_router = fastapi.APIRouter()

    if settings.ENVIRONMENT == "local":

        @_frontend_router.api_route(
            "/{path:path}",
            methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
        )
        async def proxy_to_vite(request: fastapi.Request, path: str):
            url = f"http://localhost:5173/{path}"

            if request.query_params:
                url += f"?{request.query_params}"

            try:
                async with httpx.AsyncClient() as client:
                    response = await client.request(
                        method=request.method,
                        url=url,
                        headers=dict(request.headers),
                        content=(
                            await request.body()
                            if request.method in ["POST", "PUT", "PATCH"]
                            else None
                        ),
                        timeout=30.0,
                    )

                    return fastapi.Response(
                        content=response.content,
                        status_code=response.status_code,
                        headers=dict(response.headers),
                        media_type=response.headers.get("content-type"),
                    )
            except httpx.ConnectError:
                if os.path.exists(index_path):
                    logging.warning(
                        "Vite dev server is not running, serving build output of index.html which may be stale"
                    )
                    return FileResponse(index_path)
                else:
                    return fastapi.Response(
                        content="<h1>Development Server Not Running</h1><p>Please start the Vite dev server with <code>npm run dev</code> or use <code>./scripts/dev</code></p>",
                        status_code=503,
                        media_type="text/html",
                    )
            except Exception as e:
                logging.error(f"Proxy error: {e}")
                return fastapi.Response(
                    content=f"<h1>Proxy Error</h1><p>{str(e)}</p>",
                    status_code=500,
                    media_type="text/html",
                )

    else:
        # Production mode: serve built React app as static files
        _frontend_router.mount(
            "/",
            StaticFiles(
                directory=static_files_path,
                html=True,
                check_dir=True,
            ),
            name="frontend",
        )

        @_frontend_router.get("/{full_path:path}", include_in_schema=False)
        async def frontend_router_redirect():
            return FileResponse(index_path)

    app.include_router(_frontend_router)
    yield


frontend_router = fastapi.APIRouter(lifespan=frontend_lifespan)
