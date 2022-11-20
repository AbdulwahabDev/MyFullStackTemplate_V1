from typing import Optional, Union
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from pathlib import Path
import fastapi
from fastapi.responses import RedirectResponse
from fastapi import Response, Cookie, Depends, status


from frontend_app.common.dependencies import get_verified_current, login_required

template_dir = Path(__file__).resolve().parent.parent.parent.parent.joinpath("Template")
template = Jinja2Templates(directory=template_dir)

index_router = fastapi.APIRouter(prefix="", tags=["frontend"])


@index_router.get("/")
def _(request: Request, verified_user=Depends(get_verified_current) , 
    c_token: Union[str, None] = Cookie(default=None),):

    if verified_user["status_code"] != status.HTTP_202_ACCEPTED:
        return RedirectResponse(url=verified_user["redirectUrl"])

    return template.TemplateResponse(
        "Home/index.html", {"request": request, "PageInfo": {"All_User_Info": verified_user["UserDetails"]}}
    )
