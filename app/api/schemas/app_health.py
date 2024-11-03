"""
app.api.schemas.app_health module
"""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health Response Model"""

    message: str
