from app.common.dependencies import db_session, login_required
from fastapi import APIRouter, Depends
from .schemas import Role_ModelsResponse, Role_ModelsCreateRequest, Role_ModelsUpdateRequest

from .services.list_Role_Models import get_list_Role_Models_
from .services.add_new_Role_Model import add_new_Role_Model_
from .services.get_a_Role_Model_by_id import get_a_Role_Model_by_id_
from .services.update_a_Role_Model_by_id import update_a_Role_Model_by_id_
# from .services.delete_a_Role_Model_by_id import delete_a_Role_Model_by_id_

role_models_router = APIRouter(prefix="/role_models", tags=["role_models"])

@role_models_router.get("", response_model=list[Role_ModelsResponse], dependencies=[Depends(login_required)])
def get_list_Role_Models(db_session=db_session):
    return get_list_Role_Models_(db_session)

@role_models_router.get("/{model_id}", response_model=Role_ModelsResponse, dependencies=[Depends(login_required)])
def get_a_Role_Model_by_id(model_id: str, db_session=db_session):
    return get_a_Role_Model_by_id_(model_id, db_session)

@role_models_router.post("", response_model=Role_ModelsResponse, dependencies=[Depends(login_required)])
def add_new_Role_Model(body: Role_ModelsCreateRequest, db_session=db_session):
    return add_new_Role_Model_(body, db_session)

@role_models_router.put("/{model_id}", response_model=Role_ModelsResponse, dependencies=[Depends(login_required)])
def update_a_Role_Model_by_id(model_id: str, body: Role_ModelsUpdateRequest, db_session=db_session):
    return update_a_Role_Model_by_id_(model_id, body, db_session)

# @role_models_router.delete("/{model_id}", dependencies=[Depends(login_required)])
# def delete_a_Role_Model_by_id(model_id: str, db_session=db_session):
#     return delete_a_Role_Model_by_id_(model_id=model_id,db_session=db_session)