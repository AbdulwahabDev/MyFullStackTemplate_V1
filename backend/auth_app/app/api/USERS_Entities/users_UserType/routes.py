from app.common.dependencies import db_session, login_required
from fastapi import APIRouter, Depends
from .schemas import user_UsersTypeResponse, user_UsersTypeCreateRequest, user_UsersTypeUpdateRequest

from .services.list_user_UsersType import get_list_user_UsersType_
from .services.add_new_user_UsersType import add_new_user_UsersType_
from .services.get_a_user_UsersType_by_id import get_a_users_UserType_by_id_
from .services.update_a_user_UsersType_by_id import update_a_user_UsersType_by_id_
from .services.delete_a_user_UsersType_by_id import delete_a_user_UsersType_by_id_


user_usertype_router = APIRouter(prefix="/user_usertype", tags=["user_usertype"])


@user_usertype_router.get("", response_model=list[user_UsersTypeResponse], dependencies=[Depends(login_required)])
def get_list_user_UsersType(db_session=db_session):
    return get_list_user_UsersType_(db_session)


@user_usertype_router.get(
    "/{user_id}/{userType_id}", response_model=user_UsersTypeResponse, dependencies=[Depends(login_required)]
)
def get_a_users_UserType_by_id(user_id: str, userType_id: str, db_session=db_session):
    return get_a_users_UserType_by_id_(user_id, userType_id, db_session)


@user_usertype_router.post("", response_model=user_UsersTypeResponse, dependencies=[Depends(login_required)])
def create_a_user_UsersType_(body: user_UsersTypeCreateRequest, db_session=db_session):
    return add_new_user_UsersType_(body, db_session)


@user_usertype_router.put(
    "/{user_id}/{userType_id}", response_model=user_UsersTypeResponse, dependencies=[Depends(login_required)]
)
def update_a_user_UsersType_by_id(
    user_id: str, userType_id: str, body: user_UsersTypeUpdateRequest, db_session=db_session
):
    return update_a_user_UsersType_by_id_(user_id, userType_id, body, db_session)

@user_usertype_router.delete(
    "/{user_id}/{userType_id}", dependencies=[Depends(login_required)]
)
def delete_a_user_UserType_by_id(
    user_id: str, userType_id: str, db_session=db_session
):
    return delete_a_user_UsersType_by_id_(user_id=user_id,usertype_id=userType_id,db_session=db_session)