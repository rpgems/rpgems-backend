from sqlalchemy import event

from app.adapters.repositories.database import DatabaseRepositoryImpl
from tests.integration.app.core.settings_test import get_test_settings


class TestDatabaseRepositoryImpl(DatabaseRepositoryImpl):

    def __init__(self, db):
        super().__init__(db)
        config = get_test_settings()
        self.schema = config.schema
        self.sync_engine = db.sync_engine

        @event.listens_for(self.sync_engine, "connect")
        def set_search_path(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            try:
                cursor.execute(f"SET search_path TO {self.schema}")
            finally:
                cursor.close()
