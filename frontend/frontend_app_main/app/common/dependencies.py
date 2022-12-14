import os
from typing import Optional , Union
 
from app.config import config
from fastapi import Depends, HTTPException, status , Cookie

 

import requests 
 

def get_verified_current(
    c_token: Union[str, None] = Cookie(default=None)
    
):


    if  c_token is None or c_token == 'None':
        return {
                "status_code":status.HTTP_401_UNAUTHORIZED,
                "redirectUrl":'/signin',
                "detail":"NO Token Found !"
                }
        # raise HTTPException(status.HTTP_401_UNAUTHORIZED, "NO Token Found !")
        
    AUTH_APP_URL = os.environ.get('AUTH_APP_URL')
    url = f"{AUTH_APP_URL}/users/get_verified_current_user_or_none"

    payload={}
    headers = {
        'Cookie': f'c_token={c_token}'
    }

    varified_and_decoded_token = requests.request("GET", url, headers=headers, data=payload)
    
    try: 
        if varified_and_decoded_token.status_code == 200:
            return {"status_code":status.HTTP_202_ACCEPTED , "UserDetails":eval(varified_and_decoded_token.text)} 
        else:
            try:
                return {
                        "status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,
                        "redirectUrl":'/signin',
                        "detail":varified_and_decoded_token.text
                        }
            except: 
                return {
                        "status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,
                        "redirectUrl":'/signin'
                        }
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(ex))
    
def login_required(verified_user: Optional[dict] = Depends(get_verified_current)):

    if(verified_user['status_code'] != status.HTTP_202_ACCEPTED):
        raise HTTPException(
            status_code=verified_user['status_code'],
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
      
def Project_owner_login_required(verified_user: Optional[dict] = Depends(get_verified_current)):
    pass

