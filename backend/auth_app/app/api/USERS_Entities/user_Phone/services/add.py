from commons.exceptions import *
from sqlalchemy.orm import Session

from ..models import User_Phone
from ..schemas import User_PhoneCreateRequest


def add_(
    body: User_PhoneCreateRequest,
    db_session: Session,
):
    User_Phone_ = User_Phone(user_id=body.user_id,
                            phone=body.phone,
                            note=body.note)
    db_session.add(User_Phone_)

    try:
        db_session.flush()
        return User_Phone_
    except Exception as ex:
        Get_Exceptions_details(ex)
