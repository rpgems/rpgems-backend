"""app.main module"""
from fastapi import FastAPI
from app.core.settings import get_settings

from app.api.routes.app_health import router as app_health_router
from app.api.routes.character import router as character_router
from app.api.routes.character_attribute import router as character_attribute_router
from app.api.routes.character_class import router as character_class_router


def create_app() -> FastAPI:
    """

    :return:
    """
    settings = get_settings()

    _app = FastAPI(
        debug=settings.DEBUG,
        title=settings.name,
        version=settings.version,
        root_path=settings.root_path,
        description="A system to create and play a RPG game"
    )

    _app.include_router(app_health_router)
    _app.include_router(character_router)
    _app.include_router(character_attribute_router)
    _app.include_router(character_class_router)

    return _app


app = create_app()
