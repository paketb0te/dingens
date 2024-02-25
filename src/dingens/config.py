"""Configuration Module"""

from dataclasses import dataclass
from pathlib import Path

from dingens.backends.base import GeneratingBackend
from dingens.backends.dreamstudio import DreamstudioBackend
from dingens.backends.mock import MockBackend


@dataclass
class AppConfig:
    """Basic configuration class for the app."""

    ASSET_DIR: Path = Path(__file__).parent / "assets"
    # BACKEND: GeneratingBackend = DreamstudioBackend(asset_dir=ASSET_DIR)
    BACKEND: GeneratingBackend = MockBackend()


app_config = AppConfig()
