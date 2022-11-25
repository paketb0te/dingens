from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class UserSelection(BaseModel):
    name: str
    option: str


class GeneratedOutput(BaseModel):
    assets: list[str] = []


@dataclass
class SelectionElement:
    name: str
    options: list[str]
