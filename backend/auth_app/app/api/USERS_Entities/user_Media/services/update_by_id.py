from sqlalchemy.orm import Session

from ..helpers import get_record
from ..schemas import User_MediaUpdateRequest


def update_by_id_(id: str, body: User_MediaUpdateRequest, db_session: Session):

    User_Media_ = get_record(id=id, db_session=db_session)

    User_Media_.name = body.name 
    User_Media_.URL = body.URL

    return User_Media_
