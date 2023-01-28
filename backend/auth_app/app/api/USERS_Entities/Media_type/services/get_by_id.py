from sqlalchemy.orm import Session

from ..helpers import get_record 


def get_by_id_(id: str, db_session: Session):

    return get_record(id=id, db_session=db_session)

 