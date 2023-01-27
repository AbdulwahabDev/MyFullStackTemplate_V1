from sqlalchemy.orm import Session

from ..helpers import get_Role_Name
from ..schemas import Role_NamesUpdateRequest


def update_a_Role_Name_by_id_(
    role_id: str, 
    body: Role_NamesUpdateRequest,
    db_session: Session,):
    Role_Name_ = get_Role_Name(role_id=role_id, db_session=db_session)

    Role_Name_.name = body.name if body.name else Role_Name_.name
    Role_Name_.note = body.note if body.note else Role_Name_.note

    return Role_Name_
