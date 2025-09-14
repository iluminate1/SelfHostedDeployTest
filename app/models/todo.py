from sqlalchemy import NVARCHAR, Boolean, text
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class Todo(Base):
    __tablename__ = "todo"

    content: Mapped[str] = mapped_column(NVARCHAR(25))
    is_completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=text("FALSE"),
    )

    def __repr__(self) -> str:
        return (
            f"Todo[id={self.id}, content={self.content}, completed={self.is_completed}]"
        )
