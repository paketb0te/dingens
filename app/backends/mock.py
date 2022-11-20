"""Mock module returning a static asset"""
import asyncio
import io
from pathlib import Path

from models import GeneratedOutput, UserInput
from PIL import Image


class MockBackend:
    """Mock Backend which always returns a static asset, independent of actual user input."""

    async def generate(self, user_input: UserInput) -> GeneratedOutput:
        """Returns a static asset, independent of actual user input.

        Args:
            user_input (UserInput): User inputfrom website, will be ignored.

        Returns:
            GeneratedOutput: Contains a static asset.
        """

        print("User input: ", user_input)

        img = Image.open(fp=Path(__file__).parent / "mock_asset.png", mode="r")
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")
        img_bytes = img_byte_arr.getvalue()

        await asyncio.sleep(2)

        return GeneratedOutput(asset=img_bytes)
