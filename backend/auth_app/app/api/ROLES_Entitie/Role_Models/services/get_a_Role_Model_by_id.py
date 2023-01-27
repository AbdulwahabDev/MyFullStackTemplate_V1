from sqlalchemy.orm import Session

from ..helpers import get_Role_Model


def get_a_Role_Model_by_id_(model_id: str, db_session: Session):

    return get_Role_Model(model_id=model_id, db_session=db_session)
