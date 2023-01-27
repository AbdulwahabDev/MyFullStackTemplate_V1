from sqlalchemy.orm import Session

from ..helpers import get_USERS_ROLE
 

def delete_a_USER_ROLE_by_id_(
    log_id: str,
    db_session: Session,
):
    USERS_ROLE_ = get_USERS_ROLE(
        log_id=log_id,
        db_session=db_session,
    )

    db_session.delete(USERS_ROLE_)
    return {"Remove Done ."}
