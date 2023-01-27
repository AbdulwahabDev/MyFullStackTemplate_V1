from commons.exceptions import *
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
    except Exception as ex:
        Get_Exceptions_details(ex)
