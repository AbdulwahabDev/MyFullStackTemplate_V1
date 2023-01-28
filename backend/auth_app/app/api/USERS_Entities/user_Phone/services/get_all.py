from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import User_Phone


def get_all_(session: Session):
    stmt = select(User_Phone).order_by(User_Phone.created.desc())
    User_Phone_: list[User_Phone] = session.execute(stmt).scalars().all()
    return User_Phone_
