from pathlib import Path

from backends.base import GeneratingBackend
from backends.dreamstudio import DreamstudioBackend
from backends.mock import MockBackend
from pydantic import BaseModel, BaseSettings


class AppConfig(BaseModel):
    ASSET_DIR: Path = Path(__file__).parent / "assets"
    # BACKEND: GeneratingBackend = DreamstudioBackend(asset_dir=ASSET_DIR)
    BACKEND: GeneratingBackend = MockBackend()

    class Config:
        arbitrary_types_allowed = True


app_config = AppConfig()
