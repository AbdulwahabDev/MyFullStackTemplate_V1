from sqlalchemy.orm import Session

from ..helpers import get_user


def toggleActive_a_user_by_id_(
    username: str,
    db_session: Session,
):
    user = get_user(username=username, db_session=db_session)
    if user.is_active == "true":
        user.is_active = False
    else:
        user.is_active = True
    return user
