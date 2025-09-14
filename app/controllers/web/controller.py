from litestar import Controller, get
from litestar.response import Template


class WebController(Controller):
    include_in_schema = False
    opt = {"exclude_from_auth": True}  # noqa: RUF012

    @get(["/", "/{path: str}"])
    async def index(self, _: str | None = None) -> Template:
        return Template("index.html.j2")
