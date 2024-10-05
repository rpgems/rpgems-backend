from typing import List

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.character.exceptions import CharacterNotFound
from app.character.model import Character
from app.character.db import get_character_by_id, list_all_characters, search_characters_by_name, create_character, \
    delete_character_by_id, update_character_definition

router = APIRouter(prefix="/character", tags=["character"])


class CharacterResponse(BaseModel):
    character_definition: Character


@router.get(
    path="/{character_id}",
    responses={
        status.HTTP_200_OK: {"description": "Character found, returning character"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid character id"},
        status.HTTP_404_NOT_FOUND: {"description": "Character not found"}
    },
    response_model=CharacterResponse,
)
async def get_character(character_id: int) -> CharacterResponse:
    try:
        character_response = get_character_by_id(character_id)
    except CharacterNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    response = CharacterResponse(character_definition=character_response)
    return response


@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {"description": "Characters found, returning list of characters"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "No character found"}
    },
    response_model=List[CharacterResponse],
)
async def list_characters() -> List[CharacterResponse]:
    try:
        characters = list_all_characters()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    if len(characters) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No characters found")
    response = [CharacterResponse(character_definition=character) for character in characters]
    return response


@router.get(
    path="/search",
    responses={
        status.HTTP_200_OK: {"description": "Characters found, returning list of characters"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "No character found"}
    },
    response_model=List[CharacterResponse],
)
async def list_characters_by_name(name_search: str) -> List[CharacterResponse]:
    try:
        characters = search_characters_by_name(name_search)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    if len(characters) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No characters found")
    response = [CharacterResponse(character_definition=character) for character in characters]
    return response


@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {"description": "Character created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    },
    response_model=JSONResponse,
)
async def create_new_character(character_definition: Character) -> JSONResponse:
    try:
        character_id = create_character(character_definition)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    content = {"message": "Character created"}
    headers = {"Content-Type": "application/json", "Location": f"/character/{character_id}"}
    return JSONResponse(content=content, status_code=status.HTTP_201_CREATED, headers=headers)


@router.delete(
    path="/{character_id}",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Character deleted"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "Character not found"}
    },
    response_model=JSONResponse,
)
async def delete_character(character_id: int) -> JSONResponse:
    try:
        delete_character_by_id(character_id)
    except CharacterNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    content = {"message": "Character deleted"}
    headers = {"Content-Type": "application/json"}
    return JSONResponse(content=content, status_code=status.HTTP_204_NO_CONTENT, headers=headers)


@router.put(
    path="/{character_id}",
    responses={
        status.HTTP_200_OK: {"description": "Character updated"},
        status.HTTP_201_CREATED: {"description": "Character created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    },
    response_model=JSONResponse,
)
async def update_character(character_id: int, character_definition: Character) -> JSONResponse:
    try:
        update_character_definition(character_id, character_definition)
        content = {"message": "Character updated"}
        headers = {"Content-Type": "application/json"}
        response = JSONResponse(content=content, status_code=status.HTTP_200_OK, headers=headers)
    except CharacterNotFound as e:
        character_id = create_character(character_definition)
        content = {"message": "Character updated"}
        headers = {"Content-Type": "application/json", "Location": f"/character/{character_id}"}
        response = JSONResponse(content=content, status_code=status.HTTP_201_CREATED, headers=headers)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return response
