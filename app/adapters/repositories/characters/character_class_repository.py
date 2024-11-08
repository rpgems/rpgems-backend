"""
app.adapters.repositories.characters.character_class_repository module
"""
from abc import ABC, abstractmethod

from sqlalchemy import text

from app.adapters.repositories.base_repository import BaseRepository, T
from app.adapters.repositories.characters.schemas import CharacterClassCreate
from app.adapters.repositories.database import DatabaseRepository
from app.adapters.repositories.exceptions import DatabaseError
from app.core.common import not_implemented_error
from app.domain.character_class import CharacterClass


class CharacterClassRepository(BaseRepository, ABC):
    """
    Character class repository interface
    """
    @abstractmethod
    async def save(self, character_class: CharacterClassCreate) -> CharacterClass:
        """
        :param character_class:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.save")


class CharacterClassRepositoryImpl(CharacterClassRepository):
    """
    character class repository implementation
    """
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

    async def get_by_id(self, _id: int) -> T:
        """
        :param _id:
        """
        pass

    async def get_by_uuid(self, _id: int) -> T:
        """
        :param _id:
        """
        pass
