"""
app.adapters.repositories.base_repository module
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from pydantic import BaseModel

from app.core.common import not_implemented_error


T = TypeVar("T", bound=BaseModel)


class BaseRepository(ABC, Generic[T]):
    """
    Base class for all repositories
    """
    @abstractmethod
    async def get_by_id(self, _id: int) -> T:
        """

        :param _id:
        """
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.get_by_id")

    @abstractmethod
    async def get_by_uuid(self, _id: int) -> T:
        """

        :param _id:
        """
        raise not_implemented_error(
            method_name=f"{self.__class__.__name__}.get_by_uuid"
        )
