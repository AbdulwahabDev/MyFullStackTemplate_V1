from starlette.requests import Request
from starlette.templating import Jinja2Templates
from pathlib import Path
from fastapi import Response, APIRouter


template_dir = Path(__file__).resolve().parent.parent.parent.parent.joinpath("Template")
template = Jinja2Templates(directory=template_dir)

sign_router = APIRouter(prefix="", tags=["frontend"])


@sign_router.get("/signin")
def _(request: Request, response: Response):
    return template.TemplateResponse("authentication/signin.html", {"request": request})
