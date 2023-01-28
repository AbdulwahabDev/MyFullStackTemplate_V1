from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import Media_type


def get_all_(session: Session):
    stmt = select(Media_type).order_by(Media_type.created.desc())
    Media_type_: list[Media_type] = session.execute(stmt).scalars().all()
    return Media_type_
