from app.common.dependencies import db_session, login_required
from fastapi import APIRouter, Depends
from .schemas import User_PhoneResponse,User_PhoneCreateRequest,User_PhoneUpdateRequest

from .services.get_all import get_all_
from .services.add import add_
from .services.get_by_id import get_by_id_ , get_by_user_id_
from .services.update_by_id import update_by_id_


user_phone_router = APIRouter(prefix="/user_phone", tags=["user_Phone"])


@user_phone_router.get("", response_model=list[User_PhoneResponse], dependencies=[Depends(login_required)])
def get_all(db_session=db_session):
    return get_all_(db_session)


@user_phone_router.get("/{phone_id}", response_model=User_PhoneResponse, dependencies=[Depends(login_required)])
def get_a_userType_by_id(phone_id: str, db_session=db_session):
    return get_by_id_(phone_id, db_session)



@user_phone_router.post("", response_model=User_PhoneResponse, dependencies=[Depends(login_required)])
def add(body: User_PhoneCreateRequest, db_session=db_session):
    return add_(body, db_session)


@user_phone_router.put("/{phone_id}", response_model=User_PhoneResponse, dependencies=[Depends(login_required)])
def update_by_id(phone_id: str, body: User_PhoneUpdateRequest, db_session=db_session):
    return update_by_id_(phone_id, body, db_session)



@user_phone_router.get("/user/{user_id}", response_model=list[User_PhoneResponse], dependencies=[Depends(login_required)])
def get_a_userType_by_id(user_id: str, db_session=db_session):
    return get_by_user_id_(user_id, db_session)