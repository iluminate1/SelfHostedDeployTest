from litestar.config.csrf import CSRFConfig

from app.config.settings import settings

csrf_config = CSRFConfig(secret=settings.SECRET)
