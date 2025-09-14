from pathlib import Path

from litestar.static_files import create_static_files_router

from app.config.constants import STATIC_PATH

static_router = create_static_files_router(
    directories=[Path(__file__).parent.parent / "static"],
    path=STATIC_PATH,
    name="static",
    html_mode=True,
    opt={"exclude_from_auth": True},
)
"""Static files configuration for app."""
