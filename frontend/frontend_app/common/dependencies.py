from typing import Optional , Union
 
from frontend_app.config import config
from fastapi import Depends, HTTPException, status , Cookie
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse

from jose import jwt
from jose.exceptions import ExpiredSignatureError , JWTError


def get_verified_current(
    token: Optional[str] = Depends(OAuth2PasswordBearer(tokenUrl=config.token_APP_AUTH_URL, auto_error=False)),
    c_token: Union[str, None] = Cookie(default=None)
):

    if token is None and c_token is None :
        return {"status_code":status.HTTP_401_UNAUTHORIZED , "msg":" No Token founded" , "redirectUrl":"/signin"}

    try:
        if c_token:
            varified_and_decoded_token = jwt.decode(c_token, config.AUTH_JWT_KEY, algorithms=["HS256"])
        if token:
            varified_and_decoded_token = jwt.decode(token, config.AUTH_JWT_KEY, algorithms=["HS256"])
        xx = ''
    except ExpiredSignatureError as ex:
        return {"status_code":status.HTTP_401_UNAUTHORIZED , "msg":" ExpiredSignatureError" , "redirectUrl":"/signin"}
    except JWTError as ex:
        return {"status_code":status.HTTP_401_UNAUTHORIZED , "msg":" Token is invalid" , "redirectUrl":"/signin"}
    except Exception as ex:
        print("Exception Name : ", ex.__class__.__name__)
        print("Exception Name : ", str(ex))
        return {"status_code":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":str(ex).splitlines()[0] , "redirectUrl":"/signin"}

    return {"status_code":status.HTTP_202_ACCEPTED , "UserDetails":varified_and_decoded_token} 

 
from fastapi import Request
def login_required(request:Request , verified_user: Optional[dict] = Depends(get_verified_current)):

    if(verified_user['status_code'] != status.HTTP_202_ACCEPTED):
        raise HTTPException(
            status_code=verified_user['status_code'],
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    
    
def Project_owner_login_required(verified_user: Optional[dict] = Depends(get_verified_current)):
    pass

