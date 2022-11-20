from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..helpers import get_user, hash_password


def Change_user_Password_(
    username: str,
    old_password: str,
    new_password: str,
    db_session: Session,
):
    user = get_user(username=username, db_session=db_session)
    if user.password != hash_password(old_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="old password not match !!",
        )

    user.password = hash_password(new_password)
    return user


def reset_user_Password_(
    username: str,
    db_session: Session,
):
    user = get_user(username=username, db_session=db_session)
    user.password = hash_password("123456")
    return user
