import pytest
from sqlalchemy import text

from app.adapters.repositories.characters.character_class_repository import CharacterClassRepository, \
    CharacterClassRepositoryImpl
from app.adapters.repositories.database import DatabaseRepository
from app.core.settings import get_settings
from tests.integration.app.adapters.repositories.database import TestDatabaseRepositoryImpl
from tests.integration.app.core.container.app_test import AppContainerTest
from tests.integration.app.core.settings_test import get_test_settings


def pytest_collection_modifyitems(config, items):
    for item in items:
        if "tests/integration/" in str(item.fspath):
            item.add_marker(pytest.mark.integration)


@pytest.fixture(scope="module", autouse=True)
def override_settings_for_testing():
    from app.main import app

    """
    Overrides the default settings with test_settings.

    Since this fixture is defined with scope="module" and autouse=True,
    it does not need to be manually attached to individual tests.
    All tests within this module will automatically use this fixture.
    """
    app.dependency_overrides[get_settings] = get_test_settings
    yield
    app.dependency_overrides.pop(get_settings)


@pytest.fixture(scope="module")
def container():
    config = get_test_settings().model_dump()

    container = AppContainerTest()
    container.config.from_dict(config)
    container.init_resources()
    yield container
    container.shutdown_resources()


@pytest.fixture
def db(event_loop, container):
    db = container.db()
    yield db

    event_loop.run_until_complete(db.dispose())


ALLOWED_TABLES = [
    "character_class",
]


@pytest.fixture(autouse=True)
async def clear_db(db):
    statements = [
        text(f"DELETE FROM rpgems_test.{table};")  # noqa: S608
        for table in ALLOWED_TABLES
    ]
    async with db.connect() as conn:
        for stmt in statements:
            await conn.execute(stmt)

        await conn.commit()


# ====================== Repositories ======================

@pytest.fixture
def db_repository(db) -> DatabaseRepository:
    return TestDatabaseRepositoryImpl(db=db)


@pytest.fixture
def character_class_repository(db_repository) -> CharacterClassRepository:
    return CharacterClassRepositoryImpl(database=db_repository)
