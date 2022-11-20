from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..models import user_UserType
from ..schemas import user_UsersTypeCreateRequest

# users_UserType


def add_new_user_UsersType_(
    body: user_UsersTypeCreateRequest,
    db_session: Session,
):
    user_UserType_ = user_UserType(
        user_id=body.user_id,
        usertype_id=body.usertype_id,
        note=body.note,
    )
    db_session.add(user_UserType_)

    try:
        db_session.flush()
        return user_UserType_
    except Exception as ex:
        # I should make it better later ... such from sqlalchemy.exc import IntegrityError
        # except IntegrityError:  etc ...
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "HTTP_500_INTERNAL_SERVER_ERROR")
