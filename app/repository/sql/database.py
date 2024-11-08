"""
app.adapters.repositories.database module
"""
import logging
from abc import ABC, abstractmethod

from sqlalchemy import TextClause
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncEngine

from app.core.common import not_implemented_error
from app.repository.sql.exceptions import DatabaseError


class DatabaseRepository(ABC):
    """
    DatabaseRepository interface
    """
    @abstractmethod
    async def read(self, stmt: TextClause):
        """

        :param stmt:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.read")

    @abstractmethod
    async def write(self, stmt: TextClause):
        """

        :param stmt:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.write")


class DatabaseRepositoryImpl(DatabaseRepository):
    """
    DatabaseRepository implementation
    """
    def __init__(self, db: AsyncEngine):
        self._db = db

    async def read(self, stmt: TextClause):
        try:
            async with self._db.connect() as conn:
                return await conn.execute(stmt)
        except SQLAlchemyError as e:
            raise DatabaseError(message="Error reading from database") from e

    async def write(self, stmt: TextClause):
        try:
            async with self._db.connect() as conn:
                result = await conn.execute(stmt)
                await conn.commit()
                return result
        except SQLAlchemyError as e:
            logging.error(e)
            await conn.rollback()

            raise DatabaseError(message="Error writing on database") from e
        except Exception as e:
            raise DatabaseError(
                message="Unexpected error on database communication."
            ) from e
