from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import user_UserType


def get_list_user_UsersType_(session: Session):
    stmt = select(user_UserType).order_by(user_UserType.created.desc())
    usersType: list[user_UserType] = session.execute(stmt).scalars().all()
    return usersType
