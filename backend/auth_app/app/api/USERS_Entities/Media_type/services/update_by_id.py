from sqlalchemy.orm import Session

from ..helpers import get_record
from ..schemas import Media_typeUpdateRequest


def update_by_id_(id: str, body: Media_typeUpdateRequest, db_session: Session):

    Media_type_ = get_record(id=id, db_session=db_session)

    Media_type_.name = body.name if body.name else Media_type_.name
    Media_type_.note = body.note if body.note else Media_type_.note


    return Media_type_
