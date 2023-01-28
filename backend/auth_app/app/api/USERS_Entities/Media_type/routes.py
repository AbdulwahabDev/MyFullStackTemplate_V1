from app.common.dependencies import db_session, login_required
from fastapi import APIRouter, Depends
from .schemas import Media_typeResponse , Media_typeUpdateRequest , Media_typeCreateRequest

from .services.get_all import get_all_
from .services.add import add_
from .services.get_by_id import get_by_id_ 
from .services.update_by_id import update_by_id_


media_type_router = APIRouter(prefix="/media_type", tags=["media_type"])


@media_type_router.get("", response_model=list[Media_typeResponse], dependencies=[Depends(login_required)])
def get_all(db_session=db_session):
    return get_all_(db_session)


@media_type_router.get("/{media_id}", response_model=Media_typeResponse, dependencies=[Depends(login_required)])
def get_a_userType_by_id(media_id: str, db_session=db_session):
    return get_by_id_(media_id, db_session)



@media_type_router.post("", response_model=Media_typeResponse, dependencies=[Depends(login_required)])
def add(body: Media_typeCreateRequest, db_session=db_session):
    return add_(body, db_session)


@media_type_router.put("/{media_id}", response_model=Media_typeResponse, dependencies=[Depends(login_required)])
def update_by_id(media_id: str, body: Media_typeUpdateRequest, db_session=db_session):
    return update_by_id_(media_id, body, db_session)

 