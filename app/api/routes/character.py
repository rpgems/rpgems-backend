""""app.api.routes.character module"""

from typing import List

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.api.adapter.character import (
    adapt_get_character_by_id,
    adapt_list_characters,
    adapt_search_characters_by_name,
    adapt_create_character,
    adapt_delete_character_by_id,
    adapt_update_character_definition,
)
from app.api.schemas.character import CharacterResponse

router = APIRouter(prefix="/character", tags=["character"])


@router.get(
    path="/{character_id}",
    responses={
        status.HTTP_200_OK: {"description": "Character found, returning character"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid character id"},
        status.HTTP_404_NOT_FOUND: {"description": "Character not found"},
    },
    response_model=CharacterResponse,
)
async def get_character_by_id(character_id: int) -> CharacterResponse:
    """

    :param character_id:
    :return:
    """
    character_response = adapt_get_character_by_id(character_id)
    return character_response


@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {
            "description": "Characters found, returning list of characters"
        },
        status.HTTP_404_NOT_FOUND: {"description": "No character found"},
    },
    response_model=List[CharacterResponse],
)
async def list_characters() -> List[CharacterResponse]:
    """

    :return:
    """
    characters = adapt_list_characters()
    return characters


@router.get(
    path="/search",
    responses={
        status.HTTP_200_OK: {
            "description": "Characters found, returning list of characters"
        },
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "No character found"},
    },
    response_model=List[CharacterResponse],
)
async def list_characters_by_name(name_search: str) -> List[CharacterResponse]:
    """

    :param name_search:
    :return:
    """
    characters = adapt_search_characters_by_name(name_search)
    return characters


@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {"description": "Character created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    },
)
async def create_new_character(character_definition: dict) -> JSONResponse:
    """

    :param character_definition:
    :return:
    """
    character_id = adapt_create_character(character_definition)
    content = {"message": "Character created"}
    headers = {
        "Content-Type": "application/json",
        "Location": f"/character/{character_id}",
    }
    return JSONResponse(
        content=content, status_code=status.HTTP_201_CREATED, headers=headers
    )


@router.delete(
    path="/{character_id}",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Character deleted"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "Character not found"},
    },
)
async def delete_character(character_id: int) -> JSONResponse:
    """

    :param character_id:
    :return:
    """
    adapt_delete_character_by_id(character_id)
    content = {"message": "Character deleted"}
    headers = {"Content-Type": "application/json"}
    return JSONResponse(
        content=content, status_code=status.HTTP_204_NO_CONTENT, headers=headers
    )


@router.put(
    path="/{character_id}",
    responses={
        status.HTTP_200_OK: {"description": "Character updated"},
        status.HTTP_201_CREATED: {"description": "Character created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    },
)
async def update_character(
    character_id: int, character_definition: dict
) -> JSONResponse:
    """

    :param character_id:
    :param character_definition:
    :return:
    """
    result = adapt_update_character_definition(character_id, character_definition)
    response = JSONResponse(
        content=result["content"],
        status_code=result["status"],
        headers=result["headers"],
    )
    return response
