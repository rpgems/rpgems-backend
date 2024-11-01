from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from app.core.common import not_implemented_error

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    async def get_by_id(self, _id: int) -> T:
        raise not_implemented_error(method_name=f"{self.__class__.__name__}.get_by_id")

    @abstractmethod
    async def get_by_uuid(self, _id: int) -> T:
        raise not_implemented_error(
            method_name=f"{self.__class__.__name__}.get_by_uuid"
        )
