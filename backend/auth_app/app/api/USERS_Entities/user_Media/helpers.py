from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import User_Media


def get_record(id: str, db_session: Session) -> User_Media:
    stmt = select(User_Media).where(User_Media.id == id)
    User_Media_: User_Media | None = db_session.execute(stmt).scalar_one_or_none()

    if User_Media_ is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User_Media NOT_FOUND')

    return User_Media_


def get_record_by_user_id(user_id: str, db_session: Session) -> User_Media:
    stmt = select(User_Media).where(User_Media.user_id == user_id)
    User_Media_: User_Media | None = db_session.execute(stmt).scalars().all()

    if User_Media_ is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User_Media NOT_FOUND')

    return User_Media_

def get_record_by_media_id(media_type_id: str, db_session: Session) -> User_Media:
    stmt = select(User_Media).where(User_Media.media_type_id == media_type_id)
    User_Media_: User_Media | None = db_session.execute(stmt).scalars().all()

    if User_Media_ is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User_Media NOT_FOUND')

    return User_Media_
