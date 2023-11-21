import logging

from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    LOG_LEVEL: int = logging.INFO

    DB_SERVER: str = "db_server"
    DB_USER: str = "db_user"
    DB_PASSWORD: str = "db_password"
    DB_DB: str = "db"

    @computed_field  # type: ignore[misc]
    @property
    def DB_URI_ASYNC(self) -> PostgresDsn:
        return PostgresDsn(f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}" f"@{self.DB_SERVER}/{self.DB_DB}")

    model_config = SettingsConfigDict(case_sensitive=True)


settings = AppSettings()
