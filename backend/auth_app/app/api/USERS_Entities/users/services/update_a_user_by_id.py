from sqlalchemy.orm import Session

from ..helpers import get_user_by_id
from ..schemas import UserUpdateRequest


def update_a_user_by_id_(
    id: str,
    body: UserUpdateRequest,
    db_session: Session,
):
    user = get_user_by_id(id=id, db_session=db_session)
    if body.email:
        user.email = body.email
    if body.name:
        user.name = body.name
    if body.photo:
        user.photo = body.photo
    return user
