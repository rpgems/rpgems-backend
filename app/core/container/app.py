""" Container for dependency injections. """

import httpx
from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine

from app.adapters.repositories.characters.character_class_repository import (
    CharacterClassRepositoryImpl,
)
from app.adapters.repositories.database import DatabaseRepositoryImpl
from app.core.settings import get_settings
from app.services.character_class import CreateCharacterClassServiceImpl


class AppContainer(containers.DeclarativeContainer):
    """
    AppContainer defines the creation of objects that will be injected
    into the app.api.routes module.
    """

    wiring_config = containers.WiringConfiguration(packages=["app.api.routes"])

    config = providers.Configuration()
    settings = get_settings()
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

    db_transaction = providers.Singleton(
        create_async_engine,
        settings.db_dsn,
        isolation_level=config.get("isolation_level_transaction"),
        pool_size=config.get("db_max_pool_size"),
        max_overflow=config.get("db_overflow_size"),
        pool_recycle=config.get("db_pool_recycle"),
        pool_pre_ping=True,
        echo=config.get("db_echo"),
        echo_pool=config.get("db_echo_pool"),
    )

    async_http_client = providers.Resource(
        httpx.AsyncClient,
    )

    # Database Repositories
    db_repository = providers.Factory(DatabaseRepositoryImpl, db=db)

    character_class_repository = providers.Factory(
        CharacterClassRepositoryImpl, database=db_repository
    )

    # Services
    create_character_class_service = providers.Factory(
        CreateCharacterClassServiceImpl,
        character_class_repository=character_class_repository,
    )
