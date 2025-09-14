from litestar.plugins.sqlalchemy import repository
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Todo


class TodoRepository(repository.SQLAlchemyAsyncRepository[Todo]):
    model_type = Todo


async def provide_todo_repo(db_session: AsyncSession) -> TodoRepository:
    return TodoRepository(session=db_session)
