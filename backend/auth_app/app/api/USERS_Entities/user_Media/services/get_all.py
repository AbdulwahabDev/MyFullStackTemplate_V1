from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import User_Media


def get_all_(session: Session):
    stmt = select(User_Media).order_by(User_Media.created.desc())
    User_Media_: list[User_Media] = session.execute(stmt).scalars().all()
    return User_Media_
