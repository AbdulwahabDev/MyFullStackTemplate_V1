from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import UserType


def get_userType(userType_id: str, db_session: Session) -> UserType:
    stmt = select(UserType).where(UserType.id == userType_id)
    userType: UserType | None = db_session.execute(stmt).scalar_one_or_none()

    if userType is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='UserType NOT_FOUND')

    return userType
