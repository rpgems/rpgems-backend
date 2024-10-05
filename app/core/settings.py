from os import environ

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    name: str = "RPMGems"
    version: str = "0.1"
    DEBUG: bool = True
    DESCRIPTION: str = environ.get("DESCRIPTION", "TEST Environment")

    # Application configuration
    env: str = environ.get("FASTAPI_ENV", "dev")
    API_V1_STR: str = environ.get("API_V1_STR", "/api/v1")
    FRONTEND_HOST: str = environ.get("FRONTEND_HOST", "http://localhost:8080")


@lru_cache
def get_settings() -> Settings:
    return Settings()
