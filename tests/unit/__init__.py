from typing import Dict
from unittest.mock import MagicMock

from app.core.container.app import AppContainer


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


class DatabaseResult:
    def __init__(self, stored_data: Dict):
        self._mapping = stored_data

    def fetchone(self):
        return self


def override_db_repository() -> MagicMock:
    test_container = AppContainer()
    async_mock = AsyncMock()
    test_container.db_repository.override(async_mock)
    return async_mock
