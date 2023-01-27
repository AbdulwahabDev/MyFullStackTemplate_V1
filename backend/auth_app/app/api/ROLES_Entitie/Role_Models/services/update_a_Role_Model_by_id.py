from sqlalchemy.orm import Session

from ..helpers import get_Role_Model
from ..schemas import Role_ModelsUpdateRequest


def update_a_Role_Model_by_id_(
    model_id: str, 
    body: Role_ModelsUpdateRequest,
    db_session: Session,
):
    Role_Model_ = get_Role_Model(model_id=model_id, db_session=db_session)

    Role_Model_.name = body.name if body.name else Role_Model_.name
    Role_Model_.note = body.note if body.note else Role_Model_.note

    return Role_Model_
