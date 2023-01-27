from sqlalchemy.orm import Session

from ..helpers import get_user_UserType


def delete_a_user_UsersType_by_id_(
    user_id: str,
    usertype_id: str,
    db_session: Session,
):
    usersType = get_user_UserType(
        user_id=user_id,
        usertype_id=usertype_id,
        db_session=db_session,
    )

    db_session.delete(usersType)
    return {"Remove Done ."}
