from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import User_Phone


def get_record(id: str, db_session: Session) -> User_Phone:
    stmt = select(User_Phone).where(User_Phone.id == id)
    User_Phone_: User_Phone | None = db_session.execute(stmt).scalar_one_or_none()

    if User_Phone_ is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User_Phone NOT_FOUND')

    return User_Phone_


def get_record_by_user_id(user_id: str, db_session: Session) -> User_Phone:
    stmt = select(User_Phone).where(User_Phone.user_id == user_id)
    User_Phone_: User_Phone | None = db_session.execute(stmt).scalars().all()

    if User_Phone_ is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User_Phone NOT_FOUND')

    return User_Phone_
