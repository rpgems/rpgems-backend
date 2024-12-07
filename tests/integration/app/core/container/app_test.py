from dependency_injector import providers

from app.core.container.app import AppContainer
from tests.integration.app.core.settings_test import get_test_settings


class AppContainerTest(AppContainer):
    config = providers.Configuration()
    settings = get_test_settings()
    config.from_dict(settings.model_dump())
