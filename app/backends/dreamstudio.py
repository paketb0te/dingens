import io
import os
import uuid
from pathlib import Path

import stability_sdk.client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from models import GeneratedOutput, UserInput
from PIL import Image

STABILITY_HOST = "grpc.stability.ai:443"
STABILITY_KEY = os.getenv("STABILITY_KEY")

api = stability_sdk.client.StabilityInference(
    host=STABILITY_HOST,
    key=STABILITY_KEY or "",
    verbose=True,
)


class DreamstudioBackend:
    def __init__(self, asset_dir: Path) -> None:
        self.asset_dir = asset_dir

    def _transform_user_input(self, user_input: UserInput) -> str:
        return user_input.image_type + user_input.image_style

    async def generate(self, user_input: UserInput) -> GeneratedOutput:
        prompt = self._transform_user_input(user_input=user_input)

        # Set up our initial generation parameters.
        answers = api.generate(
            prompt=prompt,
            seed=992446759,  # If a seed is provided, the resulting generated image will be deterministic.
            # What this means is that as long as all generation parameters remain the same, you can always recall the same image simply by generating it again.
            # Note: This isn't quite the case for Clip Guided generations, which we'll tackle in a future example notebook.
            steps=50,  # Step Count defaults to 50 if not specified here.
            cfg_scale=8.0,  # Influences how strongly your generation is guided to match your prompt.
            # Setting this value higher increases the strength in which it tries to match your prompt.
            # Defaults to 7.0 if not specified.
            width=512,  # Generation width, defaults to 512 if not included.
            height=512,  # Generation height, defaults to 512 if not included.
            samples=1,  # Number of images to generate, defaults to 1 if not included.
            sampler=generation.SAMPLER_K_DPM_2_ANCESTRAL  # Choose which sampler we want to denoise our generation with.
            # Defaults to k_lms if not specified. Clip Guidance only supports ancestral samplers.
            # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_lms)
        )

        asset_urls = []

        for resp in answers:
            for artifact in resp.artifacts:  # type: ignore
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    unique_id = uuid.uuid4()
                    img.save(self.asset_dir / f"{unique_id}.png", format="PNG")
                    asset_urls.append(f"/asset/{unique_id}")

        return GeneratedOutput(assets=asset_urls)
