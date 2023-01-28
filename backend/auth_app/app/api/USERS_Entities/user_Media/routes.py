from app.common.dependencies import db_session, login_required
from fastapi import APIRouter, Depends
from .schemas import User_MediaResponse,User_MediaCreateRequest,User_MediaUpdateRequest

from .services.get_all import get_all_
from .services.add import add_
from .services.get_by_id import get_by_id_ , get_record_by_media_type_id_ , get_record_by_user_id_
from .services.update_by_id import update_by_id_


user_media_router = APIRouter(prefix="/user_media", tags=["user_media"])


@user_media_router.get("", response_model=list[User_MediaResponse], dependencies=[Depends(login_required)])
def get_all(db_session=db_session):
    return get_all_(db_session)



@user_media_router.get("/{media_id}", response_model=User_MediaResponse, dependencies=[Depends(login_required)])
def get_a_userType_by_id(media_id: str, db_session=db_session):
    return get_by_id_(media_id, db_session)

@user_media_router.get("/media_type/{media_type_id}", response_model=User_MediaResponse, dependencies=[Depends(login_required)])
def get_record_by_media_type_id(media_type_id: str, db_session=db_session):
    return get_record_by_media_type_id_(media_type_id, db_session)

@user_media_router.get("/user/{user_id}", response_model=User_MediaResponse, dependencies=[Depends(login_required)])
def get_record_by_user_id(user_id: str, db_session=db_session):
    return get_record_by_user_id(user_id, db_session)





@user_media_router.post("", response_model=User_MediaResponse, dependencies=[Depends(login_required)])
def add(body: User_MediaCreateRequest, db_session=db_session):
    return add_(body, db_session)


@user_media_router.put("/{phone_id}", response_model=User_MediaResponse, dependencies=[Depends(login_required)])
def update_by_id(phone_id: str, body: User_MediaUpdateRequest, db_session=db_session):
    return update_by_id_(phone_id, body, db_session)

 