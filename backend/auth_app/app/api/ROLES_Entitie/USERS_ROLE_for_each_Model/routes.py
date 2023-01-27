from app.common.dependencies import db_session, login_required
from fastapi import APIRouter, Depends
from .schemas import USERS_ROLE_for_each_Model_Response, USERS_ROLE_for_each_Model_CreateRequest, USERS_ROLE_for_each_Model_UpdateRequest

from .services.list_USERS_ROLE import get_list_USERS_ROLE_
from .services.add_new_USERS_ROLE import add_new_USERS_ROLE_ 
from .services.get_a_USER_ROLE_by_id import get_a_USER_ROLE_by_user_id_
from .services.get_a_USER_ROLE_by_id import get_a_USER_ROLE_by_log_id_
from .services.update_a_USER_ROLE_by_id import update_a_USER_ROLE_by_id_
from .services.delete_a_USER_ROLE_by_id import delete_a_USER_ROLE_by_id_

users_role_router = APIRouter(prefix="/USERS_ROLE", tags=["USERS_ROLE"])

@users_role_router.get("",
  response_model=list[USERS_ROLE_for_each_Model_Response],
  dependencies=[Depends(login_required)])
def get_list_USERS_ROLE(db_session=db_session):
    return get_list_USERS_ROLE_(db_session)


@users_role_router.get("/user/{user_id}", response_model=list[USERS_ROLE_for_each_Model_Response], dependencies=[Depends(login_required)])
def get_list_USERS_ROLE_by_user_id(user_id:str,db_session=db_session):
    return get_a_USER_ROLE_by_user_id_(user_id,db_session)


@users_role_router.get("/{log_id}", response_model=USERS_ROLE_for_each_Model_Response, dependencies=[Depends(login_required)])
def get_a_USER_ROLE_by_log_id(log_id:str,db_session=db_session):
    return get_a_USER_ROLE_by_log_id_(log_id,db_session)


@users_role_router.post("", response_model=USERS_ROLE_for_each_Model_Response, dependencies=[Depends(login_required)])
def add_new_USERS_ROLE(body: USERS_ROLE_for_each_Model_CreateRequest, db_session=db_session):
    return add_new_USERS_ROLE_(body, db_session)

@users_role_router.delete("/{log_id}", dependencies=[Depends(login_required)])
def delete_a_USER_ROLE_by_id(log_id: str, db_session=db_session):
    return delete_a_USER_ROLE_by_id_(log_id=log_id
                                     ,db_session=db_session)