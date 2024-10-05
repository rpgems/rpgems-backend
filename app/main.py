from fastapi import FastAPI
from app.core.settings import get_settings

from app.api import router as main_router
from app.api.routes.character import router as character_router
from app.api.routes.character_class import router as character_class_router
from app.api.routes.character_attribute import router as character_attribute_router


def create_app() -> FastAPI:
    settings = get_settings()

    _app = FastAPI(
        debug=settings.DEBUG,
        title=settings.name,
        version=settings.version,
        description=f"{settings.DESCRIPTION}",
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )

    _app.include_router(main_router, prefix=settings.API_V1_STR)
    _app.include_router(character_router, prefix=settings.API_V1_STR)
    _app.include_router(character_class_router, prefix=settings.API_V1_STR)
    _app.include_router(character_attribute_router, prefix=settings.API_V1_STR)

    return _app


app = create_app()
