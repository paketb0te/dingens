from typing import Protocol

from models import GeneratedOutput, UserInput


class GeneratingBackend(Protocol):
    """Protocol class for backends that can generate assets fro ma user input."""

    async def generate(self, user_input: UserInput) -> GeneratedOutput:
        """Generate an asset from user input.

        Args:
            user_input (UserInput): The user input received from the frontend

        Returns:
            GeneratedOutput: The generated output, typically contains an image as asset.
        """
        ...
