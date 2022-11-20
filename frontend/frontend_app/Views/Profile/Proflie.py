
 
from starlette.templating import Jinja2Templates
from pathlib import Path 
import fastapi 
from fastapi import Depends , status  , Request
from fastapi.responses import RedirectResponse  

from frontend_app.common.dependencies import get_verified_current , login_required  



template_dir = Path(__file__).resolve().parent.parent.parent.parent.joinpath('Template')   
template = Jinja2Templates(directory=template_dir)

Proflie_router = fastapi.APIRouter(prefix="/profile",  tags=["frontend"])
  
@Proflie_router.get("")
def _(request:Request , verified_user = Depends(get_verified_current)): 

    if(verified_user['status_code'] != status.HTTP_202_ACCEPTED):
        return RedirectResponse(url=verified_user['redirectUrl'])
    
    return template.TemplateResponse("Profile/ProfileOverView.html", {"request": request ,"PageInfo" : {"All_User_Info":verified_user['UserDetails']}})
     
 