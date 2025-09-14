from litestar import Litestar

from app.config import (
    alchemy_plugin,
    cors_config,
    csrf_config,
    open_api_config,
    settings,
    static_router,
    template_config,
    vite_plugin,
)
from app.controllers import api_router, web_router

app = Litestar(
    [
        static_router,
        api_router,
        web_router,
    ],
    debug=settings.debug,
    plugins=[
        alchemy_plugin,
        vite_plugin,
    ],
    cors_config=cors_config,
    csrf_config=csrf_config,
    template_config=template_config,
    openapi_config=open_api_config,
)
