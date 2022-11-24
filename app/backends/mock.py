"""Mock module returning a static asset"""
import asyncio

from models import GeneratedOutput, UserInput


class MockBackend:
    """Mock Backend which always returns a static asset, independent of actual user input."""

    async def generate(self, user_input: UserInput) -> GeneratedOutput:
        """Returns a static asset, independent of actual user input.

        Args:
            user_input (UserInput): User inputfrom website, will be ignored.

        Returns:
            GeneratedOutput: Contains a static asset.
        """
        await asyncio.sleep(0.5)
        return GeneratedOutput(assets=["/asset/mock_asset", "/asset/foo"])
