from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import UserType


def get_list_of_userType_(session: Session):
    stmt = select(UserType).order_by(UserType.created.desc())
    userType: list[UserType] = session.execute(stmt).scalars().all()
    return userType
