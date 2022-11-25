"""Backend to get assets from the dreamstudio API"""

import asyncio
import io
import os
import uuid
from functools import partial
from pathlib import Path

import stability_sdk.client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from models import GeneratedOutput, SelectionElement, UserSelection
from PIL import Image


class DreamstudioBackend:
    def __init__(self, asset_dir: Path) -> None:
        self.asset_dir = asset_dir
        self.api = stability_sdk.client.StabilityInference(
            host="grpc.stability.ai:443",
            key=os.getenv("STABILITY_KEY", ""),
            verbose=True,
        )

    async def get_selection_elements(self) -> list[SelectionElement]:
        return [
            SelectionElement(
                name="Content",
                options=[
                    "Detailed illustration of a fantasy fire and ice dragon, blizzard concept artists, magic the gathering",
                    "Two men biking up a steep forest hill with a deep dark blue sweater and a wine red sweater.",
                ],
            ),
            SelectionElement(
                name="Style",
                options=[
                    "moebius, intricate, trending on artstation, deviantart, 8k, vibrant, high res",
                    "Oil painting. Emotional. Trending on artstation. Steep. Nordic Trees. Rustic. Artistic.",
                ],
            ),
        ]

    async def generate(self, user_selections: list[UserSelection]) -> GeneratedOutput:
        prompt = ", ".join(s.option for s in user_selections)

        # Get the asyncio event loop
        loop = asyncio.get_event_loop()
        # Run the originally blocking function in a separate thread,
        # scheduled by the default ThreadPoolExecutor ('None')
        # Use functools.partial() to pass keyword variables into the scheduled function,
        # See https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-pass-keywords
        answers = await loop.run_in_executor(
            None,
            partial(
                self.api.generate,
                prompt=prompt,
                seed=992446759,
                steps=50,  # Step Count defaults to 50 if not specified here.
                cfg_scale=8.0,
                width=512,
                height=512,
                samples=1,
                sampler=generation.SAMPLER_K_DPM_2_ANCESTRAL
                # Choose which sampler we want to denoise our generation with.
                # Defaults to k_lms if not specified.
                # Clip Guidance only supports ancestral samplers.
            ),
        )

        # Save the received images and create corresponding URLs
        # so that they can be served by the get_asset() function
        asset_urls = []
        for resp in answers:
            for artifact in resp.artifacts:  # type: ignore
                if artifact.type != generation.ARTIFACT_IMAGE:
                    continue
                img = Image.open(io.BytesIO(artifact.binary))
                unique_id = uuid.uuid4()
                img.save(self.asset_dir / f"{unique_id}.png", format="PNG")
                asset_urls.append(f"/asset/{unique_id}")

        return GeneratedOutput(assets=asset_urls)
