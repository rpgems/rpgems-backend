from typing import List

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.exceptions.character_class import CharacterClassNotFound, CharacterClassLinkedToResource
from app.models.character_class import CharacterClass
from app.crud.character_class import get_class_by_id, list_all_classes, search_classes_by_name, create_class, \
    delete_class_by_id, update_class_definition

router = APIRouter(prefix="/class", tags=["character_class"])


class CharacterClassResponse(BaseModel):
    character_class_definition: CharacterClass


@router.get(
    path="/{class_id}",
    responses={
        status.HTTP_200_OK: {"description": "Class found, returning it"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid class id"},
        status.HTTP_404_NOT_FOUND: {"description": "Class not found"}
    },
    response_model=CharacterClassResponse,
)
async def get_class(class_id: int) -> CharacterClassResponse:
    try:
        class_response = get_class_by_id(class_id)
    except CharacterClassNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    response = CharacterClassResponse(character_class_definition=class_response)
    return response


@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {"description": "Classes found, returning list of them"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "No class found"}
    },
    response_model=List[CharacterClassResponse],
)
async def list_classes() -> List[CharacterClassResponse]:
    try:
        classes = list_all_classes()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    if len(classes) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No classes found")
    response = [CharacterClassResponse(character_class_definition=character_class) for character_class in classes]
    return response


@router.get(
    path="/search",
    responses={
        status.HTTP_200_OK: {"description": "Classes found, returning list of them"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "No class found"}
    },
    response_model=List[CharacterClassResponse],
)
async def list_classes_by_name(name_search: str) -> List[CharacterClassResponse]:
    try:
        classes = search_classes_by_name(name_search)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    if len(classes) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No classes found")
    response = [CharacterClassResponse(character_class_definition=character_class) for character_class in classes]
    return response


@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {"description": "Class created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    }
)
async def create_new_class(class_definition: CharacterClass) -> JSONResponse:
    try:
        class_id = create_class(class_definition)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    content = {"message": "Class created"}
    headers = {"Content-Type": "application/json", "Location": f"/class/{class_id}"}
    return JSONResponse(content=content, status_code=status.HTTP_201_CREATED, headers=headers)


@router.delete(
    path="/{class_id}",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Class deleted"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "Class not found"},
        status.HTTP_409_CONFLICT: {"description": "Class linked to a character or attribute"}
    }
)
async def delete_class(class_id: int) -> JSONResponse:
    try:
        delete_class_by_id(class_id)
    except CharacterClassNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except CharacterClassLinkedToResource as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    content = {"message": "Class deleted"}
    headers = {"Content-Type": "application/json"}
    return JSONResponse(content=content, status_code=status.HTTP_204_NO_CONTENT, headers=headers)


@router.put(
    path="/{class_id}",
    responses={
        status.HTTP_200_OK: {"description": "Class updated"},
        status.HTTP_201_CREATED: {"description": "Class created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    }
)
async def update_class(class_id: int, class_definition: CharacterClass) -> JSONResponse:
    try:
        update_class_definition(class_id, class_definition)
        content = {"message": "Class updated"}
        headers = {"Content-Type": "application/json"}
        response = JSONResponse(content=content, status_code=status.HTTP_200_OK, headers=headers)
    except CharacterClassNotFound:
        character_id = create_class(class_definition)
        content = {"message": "Class created"}
        headers = {"Content-Type": "application/json", "Location": f"/class/{character_id}"}
        response = JSONResponse(content=content, status_code=status.HTTP_201_CREATED, headers=headers)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return response
