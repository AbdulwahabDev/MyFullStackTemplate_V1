from typing import Optional
from starlette.requests import Request 
from starlette.templating import Jinja2Templates
from pathlib import Path 
import fastapi
from fastapi.responses import RedirectResponse
from fastapi import Response , Cookie

template_dir = Path(__file__).resolve().parent.parent.parent.parent.joinpath('Template')   
template = Jinja2Templates(directory=template_dir)
shared_router = fastapi.APIRouter(prefix="",  tags=["frontend"])
 
@shared_router.get('/signout')
def _(response : Response): 
    response.delete_cookie('c_token')
    return "signout pass"
 