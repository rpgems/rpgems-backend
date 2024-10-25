"""app.api module"""
from fastapi import APIRouter

from app.api.routes.app_router import router as app_router

router = APIRouter()

router.include_router(app_router)
