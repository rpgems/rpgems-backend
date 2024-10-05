from typing import List

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.exceptions.character_attribute import CharacterAttributeNotFound, CharacterAttributeLinkedToResource
from app.models.character_attribute import Attribute
from app.crud.character_attribute import get_attribute_by_id, list_all_attributes, search_attributes_by_name, \
    create_attribute, delete_attribute_by_id, update_attribute_definition

router = APIRouter(prefix="/attribute", tags=["character_attribute"])


class CharacterAttributeResponse(BaseModel):
    character_attribute_definition: Attribute


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
    try:
        attribute_response = get_attribute_by_id(attribute_id)
    except CharacterAttributeNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    response = CharacterAttributeResponse(character_definition=attribute_response)
    return response


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
    try:
        attributes = list_all_attributes()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    if len(attributes) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No attributes found")
    response = [CharacterAttributeResponse(character_attribute_definition=attribute) for attribute in attributes]
    return response


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
    try:
        attributes = search_attributes_by_name(name_search)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    if len(attributes) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No attributes found")
    response = [CharacterAttributeResponse(character_attribute_definition=attribute) for attribute in attributes]
    return response


@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {"description": "Character created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    }
)
async def create_new_attribute(attribute_definition: Attribute) -> JSONResponse:
    try:
        character_id = create_attribute(attribute_definition)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
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
    try:
        delete_attribute_by_id(attribute_id)
    except CharacterAttributeNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except CharacterAttributeLinkedToResource as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
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
async def update_attribute(attribute_id: int, attribute_definition: Attribute) -> JSONResponse:
    try:
        update_attribute_definition(attribute_id, attribute_definition)
        content = {"message": "Attribute updated"}
        headers = {"Content-Type": "application/json"}
        response = JSONResponse(content=content, status_code=status.HTTP_200_OK, headers=headers)
    except CharacterAttributeNotFound:
        attribute_id = create_attribute(attribute_definition)
        content = {"message": "Attribute updated"}
        headers = {"Content-Type": "application/json", "Location": f"/attribute/{attribute_id}"}
        response = JSONResponse(content=content, status_code=status.HTTP_201_CREATED, headers=headers)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return response
