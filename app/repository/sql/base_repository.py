"""
app.adapters.repositories.base_repository module
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

from pydantic import BaseModel

from app.core.common import not_implemented_error


T = TypeVar("T", bound=BaseModel)


class BaseRepository(ABC, Generic[T]):
    """
    Base class for all repositories
    """
    @abstractmethod
    async def save(self, base_model: T) -> T:
        """

        :param base_model: The base model to save
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.save")

    @abstractmethod
    async def get_by_param(self, parameter_name: str, parameter_value: any) -> T:
        """

        :param parameter_name:
        :param parameter_value:
        """
        raise not_implemented_error(
            method_name=f"{self.__class__.__name__}.get_by_param"
        )

    @abstractmethod
    async def list_by_param(self, parameter_name: str|None, parameter_value: any) -> List[T]:
        """
        :param parameter_name:
        :param parameter_value:
        :return:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.list_by_param")

    @abstractmethod
    async def update_params(self, uuid: str, param_changes: dict) -> T:
        """
        :param uuid:
        :param param_changes:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.update_params")
