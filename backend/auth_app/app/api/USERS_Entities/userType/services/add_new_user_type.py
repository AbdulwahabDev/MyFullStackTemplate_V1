from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..models import UserType
from ..schemas import UserTypeCreateRequest


def add_new_user_type_(
    body: UserTypeCreateRequest,
    db_session: Session,
):
    userType = UserType(name=body.name)
    db_session.add(userType)

    try:
        db_session.flush()
        return userType
    except Exception:
        # I should make it better later ... such from sqlalchemy.exc import IntegrityError
        # except IntegrityError:  etc ...
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "HTTP_500_INTERNAL_SERVER_ERROR")
