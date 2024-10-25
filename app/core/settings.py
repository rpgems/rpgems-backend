"""app.settings module"""

import urllib.parse

from os import environ

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

# !/usr/bin/env python
# mypy: ignore-errors


class Settings(BaseSettings):
    """Settings class"""

    # Application
    name: str = "RPMGems"
    version: str = "0.1"
    DEBUG: bool = True

    # Database configuration
    # For more information on pool configuration, read:
    # https://docs.sqlalchemy.org/en/20/core/pooling.html
    db_max_pool_size: int = 5
    db_overflow_size: int = 10
    db_pool_recycle: int = 3600  # The connection pool will be recycled every 1 hour
    db_name: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    tracking_lock_duration: int = 120

    # Application configuration
    env: str = environ.get("FASTAPI_ENV", "dev")

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file="./docker/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def db_dsn(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        )

    @property
    def _db_password_escaped_for_alembic(self) -> str:
        """Return the password escaping the special characters as required for Alembic.
        Follows recomendation on https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls.
        """
        return urllib.parse.quote_plus(self.db_password).replace("%", "%%")

    @property
    def db_dsn_sync(self) -> str:
        return f"postgresql://{self.db_user}:{self._db_password_escaped_for_alembic}@{self.db_host}/{self.db_name}"


@lru_cache
def get_settings() -> Settings:
    """

    :return:
    """
    return Settings()
