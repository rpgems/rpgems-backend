"""app.settings module"""
from os import environ

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings class"""
    # Application
    name: str = "RPMGems"
    version: str = "0.1"
    root_path: str = "/api/v1"
    DEBUG: bool = True

    # Application configuration
    env: str = environ.get("FASTAPI_ENV", "dev")


@lru_cache
def get_settings() -> Settings:
    """

    :return:
    """
    return Settings()
