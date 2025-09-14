import msgspec

from app.schema.base import BaseStruct


class TodoResponse(BaseStruct):
    id: int
    content: str
    is_completed: bool


class TodoCreate(BaseStruct):
    content: str
    is_completed: bool | None = False


class TodoPatch(BaseStruct, kw_only=True, omit_defaults=True):
    content: str | None | msgspec.UnsetType = msgspec.UNSET
    is_completed: bool | None | msgspec.UnsetType = msgspec.UNSET


class TodoCount(BaseStruct):
    count: int
