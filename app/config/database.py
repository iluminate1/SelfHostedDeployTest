from litestar.plugins.sqlalchemy import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)

from app.config.settings import settings
from app.models import Base

session_config = AsyncSessionConfig(expire_on_commit=False)
config = SQLAlchemyAsyncConfig(
    connection_string=settings.get_db_uri,
    session_config=session_config,
    create_all=True,
    metadata=Base.metadata,
)

alchemy_plugin = SQLAlchemyPlugin(config=config)
