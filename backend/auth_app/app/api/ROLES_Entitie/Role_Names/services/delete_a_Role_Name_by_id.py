from sqlalchemy.orm import Session

from ..helpers import get_Role_Name


def delete_a_Role_Name_by_id_(
    role_id: str, 
    db_session: Session,
):
    Role_Name_ = get_Role_Name(
        role_id=role_id, 
        db_session=db_session,
    )

    db_session.delete(Role_Name_)
    return {"Remove Done ."}
