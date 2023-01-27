from sqlalchemy.orm import Session

from ..helpers import get_userType
from ..schemas import UserTypeUpdateRequest


def update_a_userType_by_id_(userType_id: str, body: UserTypeUpdateRequest, db_session: Session):
    userType = get_userType(userType_id=userType_id, db_session=db_session)
    userType.name = body.name
    return userType
