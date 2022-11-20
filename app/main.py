import asyncio
from pathlib import Path

from backends.mock import MockBackend
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from models import UserInput

app = FastAPI()
templates = Jinja2Templates(directory="templates")

backend = MockBackend()


@app.post(
    "/generate",
    responses={status.HTTP_200_OK: {"content": {"image/png": {}}}},
    response_class=Response,
)
async def generate(user_input: UserInput):
    output = await backend.generate(user_input=user_input)
    return Response(content=output.asset, media_type="image/png")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        name="index.html.j2",
        context={"request": request},
    )


@app.post("/img")
async def img(user_input: UserInput):
    print(user_input)
    await asyncio.sleep(1)
    return FileResponse(path=Path(__file__).parent / "backends" / "mock_asset.png")
