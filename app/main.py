from fastapi import FastAPI
from app.core.settings import get_settings

from app.api import router as main_router
from app import character


def create_app() -> FastAPI:
    settings = get_settings()

    _app = FastAPI(
        debug=settings.DEBUG,
        title=settings.name,
        version=settings.version,
        description="A system to create and play a RPG game",
        openapi_url=f"/openapi.json",
    )

    _app.include_router(main_router)
    _app.include_router(character.router)

    return _app


app = create_app()
