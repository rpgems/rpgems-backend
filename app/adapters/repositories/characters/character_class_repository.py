from abc import ABC, abstractmethod

from sqlalchemy import text

from app.adapters.repositories.base_repository import BaseRepository
from app.adapters.repositories.characters.schemas import CharacterClassCreate
from app.adapters.repositories.database import DatabaseRepository
from app.adapters.repositories.exceptions import DatabaseError, DatabaseNotFoundError
from app.core.common import not_implemented_error
from app.domain.character_class import CharacterClass


class CharacterClassRepository(BaseRepository[CharacterClass], ABC):

    @abstractmethod
    async def save(self, character_class: CharacterClassCreate) -> CharacterClass:
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.save")


class CharacterClassRepositoryImpl(CharacterClassRepository):

    def __init__(self, database: DatabaseRepository):
        self._database = database

    async def save(self, character_class: CharacterClassCreate) -> CharacterClass:
        stmt = text(
            """
                    INSERT INTO character_class (
                    name
                ) VALUES (
                    :name
                )
                RETURNING *
                """
        ).bindparams(
            name=character_class.name,
        )

        result = await self._database.write(stmt=stmt)
        row = result.fetchone()
        if row is None:
            raise DatabaseError("Unexpected error: Operation creation failed.")

        return CharacterClass.model_validate(row._mapping)

    async def get_by_id(self, _id: int) -> CharacterClass:
        stmt = text(
            """
            SELECT * FROM character_class WHERE id = :id
            """
        ).bindparams(id=_id)

        result = await self._database.read(stmt)
        row = result.fetchone()
        if row is None:
            raise DatabaseNotFoundError(
                table_name="character_class",
                details=f"Character class with id = {_id} not found.",
            )
        return CharacterClass.model_validate(row._mapping)

    async def get_by_uuid(self, _id: int) -> CharacterClass:
        pass
