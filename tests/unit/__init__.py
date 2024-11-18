from typing import Dict
from unittest.mock import MagicMock

from app.core.container.app import AppContainer


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


class DatabaseResult:
    def __init__(self, stored_data: Dict):
        self._mapping = stored_data
        self._rows = len(self._mapping.keys())

    def fetchone(self):
        return self._mapping

    def rowcount(self):
        return self._rows

    def mappings(self):
        return self


def override_db_repository() -> MagicMock:
    test_container = AppContainer()
    async_mock = AsyncMock()
    test_container.db_repository.override(async_mock)
    return async_mock
