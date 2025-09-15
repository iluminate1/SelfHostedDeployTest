from litestar import Controller, get
from litestar.config.response_cache import CACHE_FOREVER
from litestar.response import Template


class WebController(Controller):
    include_in_schema = False
    opt = {"exclude_from_auth": True}  # noqa: RUF012

    @get(["/", "/{path: str}"], cache=CACHE_FOREVER)
    async def index(self, _: str | None = None) -> Template:
        return Template("index.html.j2")
