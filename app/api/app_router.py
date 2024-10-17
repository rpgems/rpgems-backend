"""app.api.app_router module"""
from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    message: str


@router.get(
    path="/health",
    responses={
        status.HTTP_200_OK: {"description": "Health response OK"}
    },
    response_model=HealthResponse,
)
async def health():
    """function responsible for the /health route"""
    return HealthResponse(message="It's running!")
