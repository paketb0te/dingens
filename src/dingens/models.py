"""Module containing the data models for the app."""

from pydantic import BaseModel


class UserSelection(BaseModel):
    """Represents a users choice from the Options given by a SelectionElement"""

    name: str
    option: str


class GeneratedOutput(BaseModel):
    """Contains a list of URLs pointing to the generated assets"""

    assets: list[str] = []


class SelectionElement(BaseModel):
    """Represents a list of options for a user to choose from"""

    name: str
    options: list[str]
