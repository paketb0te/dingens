"""Mock module returning a static asset"""
import asyncio

from models import GeneratedOutput, SelectionElement, UserSelection


class MockBackend:
    """Mock Backend which always returns a static asset, independent of actual user input."""

    OPTIONS = ["/asset/mock_asset", "/asset/foo"]
    SELECTION_ELEMENTS = [
        SelectionElement(name="Rider", options=["Astronaut", "Bear"]),
        SelectionElement(name="Animal", options=["Horse", "T-Rex"]),
    ]

    async def generate(self, user_selections: list[UserSelection]) -> GeneratedOutput:
        """Returns a static asset, independent of actual user input.

        Args:
            user_input (UserInput): User input from website, will be ignored.

        Returns:
            GeneratedOutput: Contains a static asset.
        """
        await asyncio.sleep(0.5)
        return GeneratedOutput(
            assets=["/asset/" + "-".join(s.option for s in user_selections)]
        )

    async def get_selection_elements(self):
        return self.SELECTION_ELEMENTS
