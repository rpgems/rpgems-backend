"""app.api.app_router module"""
from fastapi import APIRouter, status
from app.api.schema.app_health import HealthResponse


router = APIRouter(prefix="/health", tags=["health-check"])

@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {"description": "Health response OK"}
    },
    response_model=HealthResponse,
)
async def health():
    """function responsible for the /health route"""
    return HealthResponse(message="It's running!")
