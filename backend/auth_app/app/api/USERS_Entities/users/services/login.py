from datetime import datetime, timedelta

from jose import jwt
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import config

from ..helpers import hash_password
from ..models import Users
from ..schemas import UsersLoginRequest


from app.api.USERS_Entities.user_login_audit.services.add_new_audit import logIn_audit_


def login_(
    body: UsersLoginRequest,
    db_session: Session,
):

    stmt = select(Users).where(
        Users.username == body.username.lower(),
        Users.password == hash_password(body.password),
    )

    user: Users | None = db_session.execute(stmt).scalar_one_or_none()

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    logIn_audit_(user_id=user.id, user_name=user.username, name=user.name, db_session=db_session)

    access_token = genrate_jwt_for_user(user)
    return {"access_token": access_token, "username": user.username}


def genrate_jwt_for_user(user: Users):
    now = datetime.now()
    token_expire_at = now + timedelta(seconds=config.AUTH_TOKEN_EXPIRE_IN)
    payload = {
        "sub": user.id,
        "username": user.username,
        "name": user.name,
        "email": user.email,
        "iat": int(now.timestamp()),
        "exp": int(token_expire_at.timestamp()),
    }

    encoded_jwt = jwt.encode(payload, key=config.AUTH_JWT_KEY, algorithm="HS256")
    return encoded_jwt
