from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import Role_Models


def get_list_Role_Models_(session: Session):
    stmt = select(Role_Models).order_by(Role_Models.created.desc())
    Role_Models_: list[Role_Models] = session.execute(stmt).scalars().all()
    return Role_Models_
