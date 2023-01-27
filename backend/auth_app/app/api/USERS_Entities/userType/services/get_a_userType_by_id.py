from sqlalchemy.orm import Session

from ..helpers import get_userType


def get_a_userType_by_id_(userType_id: str, db_session: Session):

    return get_userType(userType_id=userType_id, db_session=db_session)
