from http.client import HTTPException
from typing import Union
from fastapi import APIRouter, Depends, status   , Request , Response

from app.common.dependencies import db_session, login_required, get_verified_current_user_or_none


from .schemas import UsersResponse, UsersCreateRequest, UsersLoginRequest, UserUpdateRequest
from .services.list_users import get_list_of_users_
from .services.get_a_user_by_id import get_user_by_id_
from .services.get_a_user_by_username import get_get_user_
from .services.add_new_user import add_new_user_
from .services.login import login_
from .services.update_a_user_by_id import update_a_user_by_id_
from .services.toggleActive_a_user_by_id import toggleActive_a_user_by_id_
from .services.Change_user_Password import Change_user_Password_, reset_user_Password_

from app.common.dependencies import get_verified_current_user_or_none



users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/get_verified_current_user_or_none" )
def get_verified_current_user_or_none_(user = Depends(get_verified_current_user_or_none)): 
    return user

@users_router.get("", response_model=list[UsersResponse], dependencies=[Depends(login_required)])
def get_list_users(db_session=db_session):
    return get_list_of_users_(db_session)


@users_router.get("/{user_id}", response_model=UsersResponse, dependencies=[Depends(login_required)])
def get_user_by_id(user_id:str,db_session=db_session):
    return get_user_by_id_(user_id=user_id,db_session=db_session)


@users_router.post("/login")
def login(_Response:Response , body: UsersLoginRequest, db_session=db_session):
    login_response = login_(body, db_session) 
    _Response.headers['access_token'] = login_response['access_token']
    return login_response


@users_router.post("" , dependencies=[Depends(login_required)])
def create_a_user(body: UsersCreateRequest, db_session=db_session):
    return add_new_user_(body, db_session)


@users_router.put("/update", response_model=UsersResponse, dependencies=[Depends(login_required)])
def update_a_user_by_id(body: UserUpdateRequest, db_session=db_session, currentUser=Depends(get_verified_current_user_or_none)):
    return update_a_user_by_id_(id=currentUser["sub"], body=body, db_session=db_session)


@users_router.put("/changepassword", response_model=UsersResponse, dependencies=[Depends(login_required)])
def Change_user_Password(old_password: str, new_password: str, db_session=db_session, currentUser=Depends(get_verified_current_user_or_none)):
    return Change_user_Password_(
        username=currentUser["username"], old_password=old_password, new_password=new_password, db_session=db_session
    )


@users_router.put("/{username}/toggleActive", response_model=UsersResponse, dependencies=[Depends(login_required)])
def toggleActive_a_user_by_id(username: str, db_session=db_session, currentUser=Depends(get_verified_current_user_or_none)):

   

    return toggleActive_a_user_by_id_(username=username,currentUser=currentUser, db_session=db_session)


@users_router.put("/{username}/resetpassword", response_model=UsersResponse, dependencies=[Depends(login_required)])
def reset_user_Password(username: str,db_session=db_session, currentUser=Depends(get_verified_current_user_or_none)): 
    return reset_user_Password_(username=username,currentUser=currentUser,db_session=db_session)
