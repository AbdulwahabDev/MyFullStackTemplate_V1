from sqlalchemy.orm import Session

from ..helpers import get_record


def get_by_id_(userType_id: str, db_session: Session):

    return get_record(userType_id=userType_id, db_session=db_session)
