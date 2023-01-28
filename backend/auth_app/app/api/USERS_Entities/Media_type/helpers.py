from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Media_type


def get_record(id: str, db_session: Session) -> Media_type:
    stmt = select(Media_type).where(Media_type.id == id)
    Media_type_: Media_type | None = db_session.execute(stmt).scalar_one_or_none()

    if Media_type_ is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Media_type NOT_FOUND')

    return Media_type_

 