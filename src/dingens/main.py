"""FastAPI app taking user input to get assets from a backend."""

from pathlib import Path

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from dingens.config import app_config
from dingens.models import UserSelection

app = FastAPI()

template_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=template_dir)

backend = app_config.BACKEND


@app.post(
    "/generate",
)
async def generate(user_selections: list[UserSelection]) -> list[str]:
    output = await backend.generate(user_selections=user_selections)
    return output.assets


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        name="index.html.j2",
        context={
            "request": request,
            "selection_elements": await backend.get_selection_elements(),
        },
    )


@app.get("/asset/{asset_id}")
async def get_asset(asset_id: str):
    path = app_config.ASSET_DIR / f"{asset_id}.png"
    if not path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )
    return FileResponse(path=app_config.ASSET_DIR / f"{asset_id}.png")
