"""app.services.character_class module"""

from abc import ABC, abstractmethod
from typing import List

from app.repository.sql.character_class_repository import (
    CharacterClassRepository,
)
from app.core.common import not_implemented_error
from app.domain.character_class import CharacterClass


class CharacterClassService(ABC):
    """
    CharacterClassService class
    """

    @abstractmethod
    async def create(self, character_class: CharacterClass) -> CharacterClass:
        """

        :param character_class:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.create")

    @abstractmethod
    async def get_by_uuid(self, character_class_uuid: str) -> CharacterClass:
        """
        :param character_class_uuid:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.get.by_uuid")

    @abstractmethod
    async def list_character_classes(self) -> List[CharacterClass]:
        """
        list all character_classes
        """
        raise not_implemented_error(
            method_name=f"{self.__class__.__name__}.list.list_character_classes")

    @abstractmethod
    async def list_character_classes_by_name(self, character_class_name: str) -> List[
        CharacterClass]:
        """
        list all character_classes by name
        """
        raise not_implemented_error(
            method_name=f"{self.__class__.__name__}.list.list_character_classes_by_name")

    @abstractmethod
    async def delete(self, character_class_uuid: str) -> bool:
        """
        delete character_class

        :param character_class_uuid:
        :return:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.delete")

    @abstractmethod
    async def update(self, character_class_uuid: str, character_class: CharacterClass) -> bool:
        """
        update character_class
        :param character_class_uuid:
        :param character_class:
        :return:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.update")


class CharacterClassServiceImpl(CharacterClassService):
    """
    CharacterClassServiceImpl class
    """

    def __init__(self, character_class_repository: CharacterClassRepository):
        self.repo = character_class_repository

    async def create(self, character_class: CharacterClass) -> CharacterClass:
        return await self.repo.save(character_class=character_class)

    async def get_by_uuid(self, character_class_uuid: str) -> CharacterClass:
        return await self.repo.get_by_param(parameter_name="uuid",
                                            parameter_value=character_class_uuid)

    async def list_character_classes(self) -> List[CharacterClass]:
        return await self.repo.list_by_param(parameter_name=None, parameter_value=None)

    async def list_character_classes_by_name(self, character_class_name: str) -> List[
        CharacterClass]:
        return await self.repo.list_by_param(parameter_name="name",
                                             parameter_value=character_class_name)

    async def delete(self, character_class_uuid: str) -> bool:
        return await self.repo.update_params(character_class_uuid=character_class_uuid,
                                             param_changes={"is_deleted": True})

    async def update(self, character_class_uuid: str, character_class: CharacterClass) -> bool:
        return await self.repo.update_params(character_class_uuid=character_class_uuid,
                                             param_changes=character_class.to_dict())
