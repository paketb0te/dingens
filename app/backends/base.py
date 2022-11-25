from typing import Protocol, runtime_checkable

from models import GeneratedOutput, SelectionElement, UserSelection


@runtime_checkable
class GeneratingBackend(Protocol):
    """Protocol class for backends that can generate assets fro ma user input."""

    async def generate(self, user_selections: list[UserSelection]) -> GeneratedOutput:
        """Generate an asset from user input.

        Args:
            user_input (UserInput): The user input received from the frontend

        Returns:
            GeneratedOutput: The generated output, typically contains an image as asset.
        """
        ...

    async def get_selection_elements(self) -> list[SelectionElement]:
        """Get a list of SelectionElements to specify options
        to choose from in the webinterface

        Returns:
            list[SelectionElement]: List of SelectionElements
        """
        ...
