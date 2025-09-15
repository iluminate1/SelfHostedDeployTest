import os
from dataclasses import dataclass
from functools import cached_property

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    DEBUG: bool = False
    SECRET: str = os.getenv("SECRET", "only-for-testing")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "user")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "db")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "database")

    @cached_property
    def get_db_uri(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()
