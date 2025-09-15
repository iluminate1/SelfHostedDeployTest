from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    debug: bool = False
    secret: str = "only-for-testing"  # noqa: S105


settings = Settings()
