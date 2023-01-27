from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Role_Models


def get_Role_Model(model_id: str, db_session: Session) -> Role_Models:
    stmt = select(Role_Models).where((Role_Models.model_id == model_id))
    Role_Models_: Role_Models | None = db_session.execute(stmt).scalar_one_or_none()

    if Role_Models_ is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Role_Models_
