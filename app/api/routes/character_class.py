from typing import List

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.api.adapter.character_class import (adapt_get_class_by_id, adapt_list_all_classes,
                                             adapt_search_classes_by_name, adapt_create_class,
                                             adapt_delete_class_by_id, adapt_update_class_definition)
from app.api.domain.character_class import CharacterClassResponse

router = APIRouter(prefix="/class", tags=["character_class"])


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
    class_response = adapt_get_class_by_id(class_id)
    return class_response


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
    classes = adapt_list_all_classes()
    return classes


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
    classes = adapt_search_classes_by_name(name_search)
    return classes


@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {"description": "Class created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    }
)
async def create_new_class(class_definition: dict) -> JSONResponse:
    class_id = adapt_create_class(class_definition)
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
    adapt_delete_class_by_id(class_id)
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
async def update_class(class_id: int, class_definition: dict) -> JSONResponse:
    result = adapt_update_class_definition(class_id, class_definition)
    response = JSONResponse(content=result['content'], status_code=result['status'], headers=result['headers'])
    return response
