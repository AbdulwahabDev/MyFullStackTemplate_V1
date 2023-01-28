from sqlalchemy.orm import Session

from ..helpers import get_record
from ..schemas import User_PhoneUpdateRequest


def update_by_id_(id: str, body: User_PhoneUpdateRequest, db_session: Session):

    User_Phone_ = get_record(id=id, db_session=db_session)

    User_Phone_.name = body.name if body.name else User_Phone_.name
    User_Phone_.note = body.note if body.note else User_Phone_.note


    return User_Phone_
