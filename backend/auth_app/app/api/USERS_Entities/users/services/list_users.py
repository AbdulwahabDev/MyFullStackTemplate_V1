from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import Users


def get_list_of_users_(session: Session):
    stmt = select(Users).order_by(Users.created.desc())
    users: list[Users] = session.execute(stmt).scalars().all()
    return users
