from functools import lru_cache
from os import environ

from pydantic_settings import SettingsConfigDict

from app.core.settings import Settings


class SettingsTest(Settings):
    env: str = environ.get("FASTAPI_ENV", "test")

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file="./docker/.env-test",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_test_settings() -> SettingsTest:
    return SettingsTest()
