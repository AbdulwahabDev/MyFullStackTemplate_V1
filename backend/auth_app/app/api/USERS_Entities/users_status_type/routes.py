from app.common.dependencies import db_session, login_required
from fastapi import APIRouter, Depends
from .schemas import Users_Status_typeCreateRequest , Users_Status_typeResponse
from .services.get_all import get_all_
from .services.add import add_
from .services.get_by_id import get_by_id_


users_status_type_router = APIRouter(prefix="/users_status_type", tags=["userType"])


@users_status_type_router.get("", response_model=list[Users_Status_typeResponse]
# , dependencies=[Depends(login_required)]
)
def get_all(db_session=db_session):
    return get_all_(db_session)


@users_status_type_router.get("/{status_id}", response_model=Users_Status_typeResponse, dependencies=[Depends(login_required)])
def get_by_id(status_id: str, db_session=db_session):
    return get_by_id_(status_id, db_session)


@users_status_type_router.post("", response_model=Users_Status_typeResponse
# , dependencies=[Depends(login_required)]
)
def add(body: Users_Status_typeCreateRequest, db_session=db_session):
    return add_(body, db_session)
 