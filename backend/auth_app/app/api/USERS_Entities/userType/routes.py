from app.common.dependencies import db_session, login_required
from fastapi import APIRouter, Depends
from .schemas import UserTypeResponse, UserTypeCreateRequest, UserTypeUpdateRequest

from .services.list_userType import get_list_of_userType_
from .services.add_new_user_type import add_new_user_type_
from .services.get_a_userType_by_id import get_a_userType_by_id_
from .services.update_a_userType_by_id import update_a_userType_by_id_


userType_router = APIRouter(prefix="/userType", tags=["userType"])


@userType_router.get("", response_model=list[UserTypeResponse], dependencies=[Depends(login_required)])
def get_list_userType(db_session=db_session):
    return get_list_of_userType_(db_session)


@userType_router.get("/{userType_id}", response_model=UserTypeResponse, dependencies=[Depends(login_required)])
def get_a_userType_by_id(userType_id: str, db_session=db_session):
    return get_a_userType_by_id_(userType_id, db_session)


@userType_router.post("", response_model=UserTypeResponse, dependencies=[Depends(login_required)])
def create_a_userType(body: UserTypeCreateRequest, db_session=db_session):
    return add_new_user_type_(body, db_session)


@userType_router.put("/{userType_id}", response_model=UserTypeResponse, dependencies=[Depends(login_required)])
def update_a_userType_by_id(userType_id: str, body: UserTypeUpdateRequest, db_session=db_session):
    return update_a_userType_by_id_(userType_id, body, db_session)
