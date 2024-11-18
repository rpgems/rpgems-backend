"""app.api.routes.character_class module"""

from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.api.adapter.character_class import (
    adapt_create_class_params,
    adapt_update_class_definition,
)
from app.api.schemas.character_class import (
    CharacterClassResponse,
    CharacterClassRequest,
)
from app.core.container.app import AppContainer
from app.services.character_class import CharacterClassService

router = APIRouter(prefix="/class", tags=["character_class"])


@router.get(
    path="/search",
    responses={
        status.HTTP_200_OK: {"description": "Classes found, returning list of them"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "No class found"},
    },
    response_model=List[CharacterClassResponse],
)
@inject
async def list_classes_by_name(name_search: str,
                               character_class_service: CharacterClassService = Depends(
                                   Provide[AppContainer.character_class_service]
                               )) -> List[CharacterClassResponse]:
    """

    :param character_class_service:
    :param name_search:
    :return:
    """
    character_classes = await character_class_service.list_character_classes_by_name(name_search)
    return [CharacterClassResponse(uuid=character_class.uuid, name=character_class.name) for
            character_class in character_classes]


@router.get(
    path="/{class_uuid}",
    responses={
        status.HTTP_200_OK: {"description": "Class found, returning it"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid class uuid"},
        status.HTTP_404_NOT_FOUND: {"description": "Class not found"},
    },
    response_model=CharacterClassResponse,
)
@inject
async def get_class(class_uuid: str,
                    character_class_service: CharacterClassService = Depends(
                        Provide[AppContainer.character_class_service]),
                    ) -> CharacterClassResponse:
    """
    Get a character class.

    :param class_uuid:
    :param character_class_service:
    :return:
    """
    character_class = await character_class_service.get_by_uuid(character_class_uuid=class_uuid)
    return CharacterClassResponse(uuid=character_class.uuid, name=character_class.name)


@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {"description": "Classes found, returning list of them"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "No class found"},
    },
    response_model=List[CharacterClassResponse],
)
@inject
async def list_classes(character_class_service: CharacterClassService = Depends(
    Provide[AppContainer.character_class_service]
)) -> List[
    CharacterClassResponse]:
    """

    :param character_class_service:
    :return:
    """

    character_classes = await character_class_service.list_character_classes()
    return [CharacterClassResponse(uuid=character_class.uuid, name=character_class.name) for
            character_class in character_classes]


@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {"description": "Class created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    },
    status_code=status.HTTP_201_CREATED,
)
@inject
async def create_new_class(
        character_class_request: CharacterClassRequest,
        character_class_service: CharacterClassService = Depends(
            Provide[AppContainer.character_class_service]
        ),
) -> CharacterClassResponse:
    """
    Creates a new Character Class.

    :param character_class_request: CharacterClassRequest;
    :param character_class_service: CreateCharacterClassService;
    :return:
    """

    character_class = adapt_create_class_params(character_class_request)

    character_class = await character_class_service.create(
        character_class=character_class
    )
    return CharacterClassResponse(uuid=character_class.uuid, name=character_class.name)


@router.delete(
    path="/{class_uuid}",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Class deleted"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "Class not found"},
        status.HTTP_409_CONFLICT: {
            "description": "Class linked to a character or attribute"
        },
    },
)
@inject
async def delete_class(class_uuid: str,
                       character_class_service: CharacterClassService = Depends(
                           Provide[AppContainer.character_class_service]
                       )) -> JSONResponse:
    """

    :param class_uuid:
    :param character_class_service:
    :return:
    """
    delete_result = await character_class_service.delete(character_class_uuid=class_uuid)
    if delete_result:
        status_code = status.HTTP_204_NO_CONTENT
        content = {"message": "Class deleted"}
        headers = {"Content-Type": "application/json"}
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        content = {"message": "Invalid request"}
        headers = {"Content-Type": "application/json"}
    return JSONResponse(
        content=content, status_code=status_code, headers=headers)


@router.put(
    path="/{class_uuid}",
    responses={
        status.HTTP_200_OK: {"description": "Class updated"},
        status.HTTP_201_CREATED: {"description": "Class created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    },
)
@inject
async def update_class(class_uuid: str, character_class_request: CharacterClassRequest,
                       character_class_service: CharacterClassService = Depends(
                           Provide[AppContainer.character_class_service]
                       )
                       ) -> JSONResponse:
    """

    :param class_uuid:
    :param character_class_request:
    :param character_class_service:
    :return:
    """
    character_class = adapt_update_class_definition(character_class_request)
    update_result = await character_class_service.update(character_class_uuid=class_uuid,
                                                         character_class=character_class)
    if update_result:
        status_code = status.HTTP_200_OK
        content = {"message": "Class updated"}
        headers = {"Content-Type": "application/json"}
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        content = {"message": "Invalid request"}
        headers = {"Content-Type": "application/json"}
    return JSONResponse(
        content=content, status_code=status_code, headers=headers)
