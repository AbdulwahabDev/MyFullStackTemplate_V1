from app.common.dependencies import db_session, login_required
from fastapi import APIRouter, Depends
from .schemas import Role_NamesResponse, Role_NamesCreateRequest, Role_NamesUpdateRequest

from .services.list_Role_Names import get_list_Role_Names_
from .services.add_new_Role_Name import add_new_Role_Name_
from .services.get_a_Role_Name_by_id import get_a_Role_Name_by_id_
from .services.update_a_Role_Name_by_id import update_a_Role_Name_by_id_
# from .services.delete_a_Role_Name_by_id import delete_a_Role_Name_by_id_

role_names_router = APIRouter(prefix="/role_names", tags=["role_names"])

@role_names_router.get("", response_model=list[Role_NamesResponse], dependencies=[Depends(login_required)])
def get_list_Role_Names(db_session=db_session):
    return get_list_Role_Names_(db_session)

@role_names_router.get("/{role_id}", response_model=Role_NamesResponse, dependencies=[Depends(login_required)])
def get_a_Role_Name_by_id(role_id: str, db_session=db_session):
    return get_a_Role_Name_by_id_(role_id, db_session)

@role_names_router.post("", response_model=Role_NamesResponse, dependencies=[Depends(login_required)])
def add_new_Role_Name(body: Role_NamesCreateRequest, db_session=db_session):
    return add_new_Role_Name_(body, db_session)

@role_names_router.put("/{role_id}", response_model=Role_NamesResponse, dependencies=[Depends(login_required)])
def update_a_Role_Name_by_id(role_id: str, body: Role_NamesUpdateRequest, db_session=db_session):
    return update_a_Role_Name_by_id_(role_id, body, db_session)
 