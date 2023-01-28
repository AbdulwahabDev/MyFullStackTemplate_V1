from commons.exceptions import *
from sqlalchemy.orm import Session

from ..models import Users_Status_type
from ..schemas import Users_Status_typeCreateRequest


def add_(
    body: Users_Status_typeCreateRequest,
    db_session: Session,
):
    users_Status_type = Users_Status_type(name=body.name,note=body.note)
    db_session.add(users_Status_type)

    try:
        db_session.flush()
        return users_Status_type
    except Exception as ex:
        Get_Exceptions_details(ex)
