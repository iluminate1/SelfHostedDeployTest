from litestar import Router

from app.controllers.api.todos import TodoAPI

api_router = Router(path="/api", route_handlers=[TodoAPI])

__all__ = ("api_router",)
