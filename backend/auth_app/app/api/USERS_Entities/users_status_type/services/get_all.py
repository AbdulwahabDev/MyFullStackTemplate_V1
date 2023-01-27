from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import Users_Status_type


def get_all_(session: Session):
    stmt = select(Users_Status_type).order_by(Users_Status_type.created.desc())
    Users_Status_type_: list[Users_Status_type] = session.execute(stmt).scalars().all()
    return Users_Status_type_
