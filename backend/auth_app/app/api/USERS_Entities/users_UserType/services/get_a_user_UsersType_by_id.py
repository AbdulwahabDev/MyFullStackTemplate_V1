from sqlalchemy.orm import Session

from ..helpers import get_user_UserType


def get_a_users_UserType_by_id_(user_id: str, userType_id: str, db_session: Session):

    return get_user_UserType(user_id=user_id, usertype_id=userType_id, db_session=db_session)
