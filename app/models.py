from pydantic import BaseModel


class UserInput(BaseModel):
    image_style: str
    image_type: str


class GeneratedOutput(BaseModel):
    assets: list[str] = []
