from config import app_config
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from models import UserInput

app = FastAPI()
templates = Jinja2Templates(directory="templates")

backend = app_config.BACKEND


@app.post(
    "/generate",
)
async def generate_new(user_input: UserInput) -> list[str]:
    output = await backend.generate(user_input=user_input)
    return output.assets


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        name="index.html.j2",
        context={"request": request},
    )


@app.get("/asset/{asset_id}")
async def img(asset_id: str):
    path = app_config.ASSET_DIR / f"{asset_id}.png"
    if path.exists():
        return FileResponse(path=app_config.ASSET_DIR / f"{asset_id}.png")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )
