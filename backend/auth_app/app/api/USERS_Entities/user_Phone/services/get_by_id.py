from sqlalchemy.orm import Session

from ..helpers import get_record , get_record_by_user_id


def get_by_id_(id: str, db_session: Session):

    return get_record(id=id, db_session=db_session)


def get_by_user_id_(user_id: str, db_session: Session):

    return get_record_by_user_id(user_id=user_id, db_session=db_session)
