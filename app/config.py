"""Configuration Module"""

from dataclasses import dataclass
from pathlib import Path

from backends.base import GeneratingBackend
from backends.dreamstudio import DreamstudioBackend
from backends.mock import MockBackend


@dataclass
class AppConfig:
    """Basic configuration class for the app."""

    ASSET_DIR: Path = Path(__file__).parent / "assets"
    # BACKEND: GeneratingBackend = DreamstudioBackend(asset_dir=ASSET_DIR)
    BACKEND: GeneratingBackend = MockBackend()


app_config = AppConfig()
