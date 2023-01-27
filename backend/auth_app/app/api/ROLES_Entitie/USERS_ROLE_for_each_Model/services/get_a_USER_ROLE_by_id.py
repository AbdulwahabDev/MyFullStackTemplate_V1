from sqlalchemy.orm import Session

from ..helpers import  get_USERS_ROLE_by_user , get_USERS_ROLE




def get_a_USER_ROLE_by_user_id_(user_id: str, db_session: Session):

    return get_USERS_ROLE_by_user(user_id=user_id , db_session=db_session)


def get_a_USER_ROLE_by_log_id_(log_id: str, db_session: Session):

    return get_USERS_ROLE(log_id=log_id , db_session=db_session)
