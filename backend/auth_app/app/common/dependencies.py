from typing import Optional, Union


from app.common.db import db
from app.config import config

from commons.dependencies import get_db_session_dependency
from fastapi import Depends, HTTPException, status , Request
from fastapi.security import OAuth2PasswordBearer

from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
security = HTTPBearer()

get_db_read_session = get_db_session_dependency(db.ReadSessionLocal)
db_read_session = Depends(get_db_read_session)

get_db_session = get_db_session_dependency(db.SessionLocal)
db_session = Depends(get_db_session)
  


def get_verified_current_user_or_none(credentials: HTTPAuthorizationCredentials= Depends(security)):
     
    if  credentials.credentials == None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "NO Token Found !") 

    try: 
        
        varified_and_decoded_token = jwt.decode(credentials.credentials,key=config.AUTH_JWT_KEY,algorithms=config.Get_HASH_ALGORITHM)

    except ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "ExpiredSignatureError")
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token is invalid")
    except Exception as ex:
        print("Exception Name : ", ex.__class__.__name__)
        print("Exception Name : ", str(ex))
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(ex).splitlines()[0])

    return varified_and_decoded_token


def login_required(payload: Optional[dict] = Depends(get_verified_current_user_or_none)):
    """
    we are sure to have the token since we have auto_error = True
    """

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
