"""
app.adapters.repositories.characters.character_class_repository module
"""
from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import text

from app.repository.sql.base_repository import BaseRepository
from app.repository.sql.database import DatabaseRepository
from app.repository.sql.exceptions import DatabaseError, NotFound
from app.core.common import not_implemented_error
from app.domain.character_class import CharacterClass


class CharacterClassRepository(BaseRepository, ABC):
    """
    Character class repository interface
    """

    @abstractmethod
    async def save(self, character_class: CharacterClass) -> CharacterClass:
        """
        :param character_class:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.save")

    @abstractmethod
    async def get_by_param(self, parameter_name: str, parameter_value: any) -> CharacterClass:
        """
        :param parameter_name:
        :param parameter_value:
        :return:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.get_by_uuid")

    @abstractmethod
    async def list_by_param(self, parameter_name: str | None, parameter_value: any) -> List[
        CharacterClass]:
        """
        :param parameter_name:
        :param parameter_value:
        :return:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.list_by_param")

    @abstractmethod
    async def update_params(self, character_class_uuid: str, param_changes: dict) -> bool:
        """
        :param character_class_uuid:
        :param param_changes:
        :return:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.delete")


class CharacterClassRepositoryImpl(CharacterClassRepository):
    """
    character class repository implementation
    """

    def __init__(self, database: DatabaseRepository):
        self._database = database

    async def save(self, character_class: CharacterClass) -> CharacterClass:
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
        if result.rowcount == 0:
            raise DatabaseError("Unexpected error: Operation creation failed.")
        row = result.mappings().fetchone()
        return CharacterClass.model_validate(row)

    async def get_by_param(self, parameter_name: str, parameter_value: any) -> CharacterClass:
        """
        :param parameter_name:
        :param parameter_value:
        """
        if parameter_name == "uuid":
            stmt = text(
                """
                SELECT * FROM character_class WHERE uuid::text = :uuid and is_deleted = FALSE
                """
            ).bindparams(uuid=parameter_value)
        else:
            raise DatabaseError("Unexpected error: Unknown parameter.")

        result = await self._database.read(stmt=stmt)
        if result.rowcount > 0:
            row = result.mappings().fetchone()
        else:
            raise NotFound("Not entity found")

        return CharacterClass.model_validate(row)

    async def list_by_param(self, parameter_name: str | None, parameter_value: any) -> List[
        CharacterClass]:
        """
        :param parameter_name:
        :param parameter_value:
        :return:
        """
        if parameter_name == "name":
            stmt = text(
                """
                SELECT * FROM character_class WHERE name = :name and is_deleted = FALSE
                """
            ).bindparams(name=parameter_value)
        else:
            stmt = text(
                """
                SELECT * FROM character_class where is_deleted = FALSE
                """
            )

        result = await self._database.read(stmt=stmt)
        if result.rowcount > 0:
            rows = result.mappings().fetchall()
        else:
            raise NotFound("No entity found.")
        character_classes = []
        for row in rows:
            character_classes.append(CharacterClass.model_validate(row))
        return character_classes

    async def update_params(self, character_class_uuid: str, param_changes: dict) -> bool:
        """
        :param character_class_uuid:
        :param param_changes:
        :return:
        """
        del param_changes["uuid"]
        del param_changes["attributes"]
        for key, value in param_changes.items():
            if key == "name":
                stmt = text(
                    """
                    UPDATE character_class SET name = :name WHERE uuid::text = :uuid
                    and is_deleted = FALSE
                    """
                ).bindparams(
                    name=value,
                    uuid=character_class_uuid
                )
                try:
                    await self._database.write(stmt=stmt)
                except Exception as e:
                    raise DatabaseError("Unexpected error: Operation update failed.") from e
            elif key == "is_deleted":
                stmt = text(
                    """
                    UPDATE character_class SET is_deleted = :is_deleted WHERE uuid::text = :uuid 
                    and is_deleted = FALSE
                    """
                ).bindparams(
                    is_deleted=value,
                    uuid=character_class_uuid
                )
                try:
                    await self._database.write(stmt=stmt)
                except Exception as e:
                    raise DatabaseError("Unexpected error: Operation update failed.") from e
            else:
                raise DatabaseError("Unexpected error: Unknown parameter.")
            return True
