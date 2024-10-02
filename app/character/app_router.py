from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel

from app.character.exceptions import CharacterNotFound
from app.character.model import Character
from app.character.db import get_character_by_id

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
