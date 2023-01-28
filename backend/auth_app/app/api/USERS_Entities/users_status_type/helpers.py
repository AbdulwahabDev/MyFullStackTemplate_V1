from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Users_Status_type


def get_record(status_id: str, db_session: Session) -> Users_Status_type:
    stmt = select(Users_Status_type).where(Users_Status_type.id == status_id)
    Users_Status_type_: Users_Status_type | None = db_session.execute(stmt).scalar_one_or_none()

    if Users_Status_type_ is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Users_Status_type_ NOT_FOUND')

    return Users_Status_type_

def get_record_by_name(name: str, db_session: Session) -> Users_Status_type:
    stmt = select(Users_Status_type).where(Users_Status_type.name == name)
    Users_Status_type_: Users_Status_type | None = db_session.execute(stmt).scalar_one_or_none()

    if Users_Status_type_ is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Users_Status_type_ NOT_FOUND')

    return Users_Status_type_
