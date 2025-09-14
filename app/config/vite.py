from litestar_vite import ViteConfig, VitePlugin

from app.config.settings import settings

vite_config = ViteConfig(
    use_server_lifespan=True,
    dev_mode=settings.debug,
    hot_reload=True,
    asset_url="/build/",
)

vite_plugin = VitePlugin(vite_config)
