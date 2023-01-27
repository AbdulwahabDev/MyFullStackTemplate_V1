from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import USERS_ROLE_for_each_Model as USERS_ROLE


def get_USERS_ROLE(log_id: str, db_session: Session) -> USERS_ROLE:
    stmt = select(USERS_ROLE).where((USERS_ROLE.log_id == log_id) )
    USERS_ROLE_: USERS_ROLE | None = db_session.execute(stmt).scalar_one_or_none()

    if USERS_ROLE_ is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return USERS_ROLE_

def get_USERS_ROLE_by_user(user_id: str, db_session: Session) -> USERS_ROLE:
    stmt = select(USERS_ROLE).where((USERS_ROLE.user_id == user_id) )
    USERS_ROLE_: USERS_ROLE | None = db_session.execute(stmt).scalars().all()

    if USERS_ROLE_ is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return USERS_ROLE_
