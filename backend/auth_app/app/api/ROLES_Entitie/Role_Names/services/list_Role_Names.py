from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import Role_Names


def get_list_Role_Names_(session: Session):
    stmt = select(Role_Names).order_by(Role_Names.created.desc())
    Role_Names_: list[Role_Names] = session.execute(stmt).scalars().all()
    return Role_Names_
