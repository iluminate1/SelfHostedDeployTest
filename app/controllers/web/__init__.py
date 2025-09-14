from litestar import Router

from app.controllers.web.controller import WebController

web_router = Router(path="/", route_handlers=[WebController])

__all__ = ("web_router",)
