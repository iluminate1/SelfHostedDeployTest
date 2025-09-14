from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin, SwaggerRenderPlugin

scalar_plugin = ScalarRenderPlugin()
swagger_plugin = SwaggerRenderPlugin(path="/")

open_api_config = OpenAPIConfig(
    title="Todo API",
    version="1",
    path="/docs",
    render_plugins=[scalar_plugin, swagger_plugin],
)
