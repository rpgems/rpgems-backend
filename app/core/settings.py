from os import environ

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    name: str = "RPMGems"
    version: str = f"0.1"
    DEBUG: bool = True

    # Application configuration
    env: str = environ.get("FASTAPI_ENV", "dev")


@lru_cache
def get_settings() -> Settings:
    return Settings()
