import logging
from abc import ABC, abstractmethod

from sqlalchemy import TextClause
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncEngine

from app.core.common import not_implemented_error
from app.adapters.repositories.exceptions import DatabaseError


class DatabaseRepository(ABC):
    @abstractmethod
    async def read(self, stmt: TextClause):
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.read")

    @abstractmethod
    async def write(self, stmt: TextClause):
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.write")


class DatabaseRepositoryImpl(DatabaseRepository):
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
