from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Role_Names


def get_Role_Name(role_id: str, db_session: Session) -> Role_Names:
    stmt = select(Role_Names).where((Role_Names.role_id == role_id))
    Role_Names_: Role_Names | None = db_session.execute(stmt).scalar_one_or_none()

    if Role_Names_ is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Role_Names_
