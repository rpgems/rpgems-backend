from typing import List

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from app.api.adapter.character_attribute import (adapt_get_attribute_by_id, adapt_list_all_attributes,
                                                 adapt_search_attributes_by_name, adapt_create_attribute,
                                                 adapt_delete_attribute_by_id, adapt_update_attribute_definition)
from app.api.domain.character_attribute import CharacterAttributeResponse


router = APIRouter(prefix="/attribute", tags=["character_attribute"])


@router.get(
    path="/{attribute_id}",
    responses={
        status.HTTP_200_OK: {"description": "Attribute found, returning it"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid attribute id"},
        status.HTTP_404_NOT_FOUND: {"description": "Attribute not found"}
    },
    response_model=CharacterAttributeResponse,
)
async def get_attribute(attribute_id: int) -> CharacterAttributeResponse:
    attribute_response = adapt_get_attribute_by_id(attribute_id)
    return attribute_response


@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {"description": "Attributes found, returning list of them"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "No attribute found"}
    },
    response_model=List[CharacterAttributeResponse],
)
async def list_attribute() -> List[CharacterAttributeResponse]:
    attributes = adapt_list_all_attributes()
    return attributes


@router.get(
    path="/search",
    responses={
        status.HTTP_200_OK: {"description": "Attributes found, returning list of them"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "No attribute found"}
    },
    response_model=List[CharacterAttributeResponse],
)
async def list_attributes_by_name(name_search: str) -> List[CharacterAttributeResponse]:
    attributes = adapt_search_attributes_by_name(name_search)
    return attributes


@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {"description": "Character created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    }
)
async def create_new_attribute(attribute_definition: dict) -> JSONResponse:
    character_id = adapt_create_attribute(attribute_definition)
    content = {"message": "Attribute created"}
    headers = {"Content-Type": "application/json", "Location": f"/attribute/{character_id}"}
    return JSONResponse(content=content, status_code=status.HTTP_201_CREATED, headers=headers)


@router.delete(
    path="/{attribute_id}",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Attribute deleted"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
        status.HTTP_404_NOT_FOUND: {"description": "Attribute not found"},
        status.HTTP_409_CONFLICT: {"description": "Attribute linked to a class or character"},
    }
)
async def delete_attribute(attribute_id: int) -> JSONResponse:
    adapt_delete_attribute_by_id(attribute_id)
    content = {"message": "Attribute deleted"}
    headers = {"Content-Type": "application/json"}
    return JSONResponse(content=content, status_code=status.HTTP_204_NO_CONTENT, headers=headers)


@router.put(
    path="/{attribute_id}",
    responses={
        status.HTTP_200_OK: {"description": "Attribute updated"},
        status.HTTP_201_CREATED: {"description": "Attribute created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    }
)
async def update_attribute(attribute_id: int, attribute_definition: dict) -> JSONResponse:
    result = adapt_update_attribute_definition(attribute_id, attribute_definition)
    response = JSONResponse(content=result['content'], status_code=result['status'], headers=result['headers'])
    return response
