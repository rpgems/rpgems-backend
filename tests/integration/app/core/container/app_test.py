from dependency_injector import containers, providers
from app.core.container.app import AppContainer
from tests.integration.app.core.settings_test import get_test_settings
from sqlalchemy.ext.asyncio import create_async_engine


class AppContainerTest(AppContainer):
    config = providers.Configuration()
    settings = get_test_settings()
    config.from_dict(settings.model_dump())

    db = providers.Singleton(
        create_async_engine,
        settings.db_dsn,
        isolation_level=config.get("isolation_level"),
        pool_size=config.get("db_max_pool_size"),
        max_overflow=config.get("db_overflow_size"),
        pool_recycle=config.get("db_pool_recycle"),
        pool_pre_ping=True,
        echo=config.get("db_echo"),
        echo_pool=config.get("db_echo_pool"),
    )