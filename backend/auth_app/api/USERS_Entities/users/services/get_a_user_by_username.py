from sqlalchemy.orm import Session

from ..helpers import get_user


def get_get_user_(username: str, db_session: Session): 
    return get_user(username=username, db_session=db_session)
