import logging
import os
import sys
from contextlib import asynccontextmanager

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.app.api.v1.api import api_router
from backend.app.core.config import settings
from backend.app.utils.logger import setup_logging

setup_logging()
logger = logging.getLogger("terraverse")

APP_VERSION = getattr(settings, "VERSION", "0.1.0")
APP_ENV = getattr(settings, "ENV", "development")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown lifecycle event handler."""
    logger.info(
        f"Starting TerraVerse Backend API v{APP_VERSION} [{APP_ENV.upper()}]"
    )
    yield
    logger.info("Shutting down TerraVerse Backend API cleanly...")


app = FastAPI(
    title=getattr(settings, "PROJECT_NAME", "TerraVerse API"),
    version=APP_VERSION,
    description="TerraVerse Spatial Intelligence & Land Record Harmonization Platform API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Configure CORS settings
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

configured_origins = getattr(settings, "BACKEND_CORS_ORIGINS", [])
if configured_origins:
    origins.extend([str(origin) for origin in configured_origins])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=getattr(settings, "API_V1_STR", "/api/v1"))


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error on request {request.url}: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "An internal server error occurred.",
            "error_message": str(exc) if getattr(settings, "DEBUG", False) else "Internal Error",
        },
    )


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for container orchestrators and load balancers."""
    return {
        "status": "HEALTHY",
        "project": getattr(settings, "PROJECT_NAME", "TerraVerse API"),
        "version": APP_VERSION,
        "environment": APP_ENV,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=getattr(settings, "DEBUG", True),
    )