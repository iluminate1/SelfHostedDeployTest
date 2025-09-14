from collections.abc import Sequence

from litestar import Controller, delete, get, patch, post
from litestar.di import Provide

from app.models import Todo
from app.repo.todos import TodoRepository, provide_todo_repo
from app.schema.todo import TodoCount, TodoCreate, TodoPatch, TodoResponse


class TodoAPI(Controller):
    path = "/todos"
    dependencies = {  # noqa: RUF012
        "todo_repo": Provide(provide_todo_repo),
    }
    tags = ["Todos"]  # noqa: RUF012

    @get("/")
    async def get_todos(
        self,
        todo_repo: TodoRepository,
    ) -> Sequence[Todo]:
        return await todo_repo.list()

    @get("/count")
    async def get_todos_count(self, todo_repo: TodoRepository) -> TodoCount:
        count = await todo_repo.count()
        return TodoCount(count=count)

    @post("/")
    async def create_todo(
        self,
        data: TodoCreate,
        todo_repo: TodoRepository,
    ) -> TodoResponse:
        todo = await todo_repo.add(Todo(**data.as_dict()))
        await todo_repo.session.commit()
        return TodoResponse(**todo.to_dict())

    @patch("/{todo_id:int}/toggle")
    async def patch_todo_status(
        self,
        todo_id: int,
        todo_repo: TodoRepository,
    ) -> TodoResponse:
        todo = await todo_repo.get_one(id=todo_id)
        todo.is_completed = not todo.is_completed
        await todo_repo.session.commit()

        return TodoResponse(
            **todo.to_dict(),
        )

    @patch("/{todo_id:int}")
    async def patch_todo(
        self,
        todo_id: int,
        data: TodoPatch,
        todo_repo: TodoRepository,
    ) -> TodoResponse:
        raw_obj = data.to_builtins()
        raw_obj["id"] = todo_id
        todo = Todo(**raw_obj)

        updated_todo = await todo_repo.update(todo)
        await todo_repo.session.commit()

        return TodoResponse(**updated_todo.to_dict())

    @delete("/{todo_id:int}")
    async def delete_todo(self, todo_id: int, todo_repo: TodoRepository) -> None:
        await todo_repo.delete(todo_id)
        await todo_repo.session.commit()
