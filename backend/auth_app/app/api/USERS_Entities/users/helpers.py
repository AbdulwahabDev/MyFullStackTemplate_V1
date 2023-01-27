import bcrypt
from app.config import config

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.api.USERS_Entities.users.models import Users


def hash_password(password: str):
    hashed_bytes = bcrypt.kdf(
        password=password.encode("UTF-8"),
        salt=config.AUTH_SALT.encode("UTF-8"),
        desired_key_bytes=32,
        rounds=100,
    )

    password = str(hashed_bytes)
    return password


def get_user(username: str, db_session: Session) -> Users:
    stmt = select(Users).where(Users.username == username.lower())
    user: Users | None = db_session.execute(stmt).scalar_one_or_none()

    return user


def get_user_by_id(id: str, db_session: Session) -> Users:
    stmt = select(Users).where(Users.id == id)
    user: Users | None = db_session.execute(stmt).scalar_one_or_none()

    return user
