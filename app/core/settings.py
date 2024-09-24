import urllib.parse
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Application
    name: str = "RPMGems"
    version: str = f"0.1"
    DEBUG: bool = True

    # Application configuration
    env: str  # dev, test, ci, prod

    model_config = SettingsConfigDict(
        env_prefix="APP_", env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

@lru_cache
def get_settings(env: str | None = None) -> Settings:
    return Settings()  # type: ignore
