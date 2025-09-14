from litestar.plugins.sqlalchemy import BigIntBase


class Base(BigIntBase):
    __abstract__ = True
