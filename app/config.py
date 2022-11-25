"""Configuration Module"""

from pathlib import Path

from backends.base import GeneratingBackend
from backends.dreamstudio import DreamstudioBackend
from backends.mock import MockBackend
from pydantic import BaseModel


class AppConfig(BaseModel):
    """Basic configuration class for the app."""

    ASSET_DIR: Path = Path(__file__).parent / "assets"
    # BACKEND: GeneratingBackend = DreamstudioBackend(asset_dir=ASSET_DIR)
    BACKEND: GeneratingBackend = MockBackend()

    class Config:
        """meta-configuration for the AppConfig class itself."""

        arbitrary_types_allowed = True


app_config = AppConfig()
