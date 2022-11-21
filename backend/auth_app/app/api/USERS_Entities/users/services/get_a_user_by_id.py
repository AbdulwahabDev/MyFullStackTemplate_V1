from sqlalchemy.orm import Session

from ..helpers import get_user_by_id


def get_user_by_id_(user_id: str, db_session: Session): 
    return get_user_by_id(id=user_id, db_session=db_session)
