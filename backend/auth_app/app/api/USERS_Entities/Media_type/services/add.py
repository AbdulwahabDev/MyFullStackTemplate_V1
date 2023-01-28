from commons.exceptions import *
from sqlalchemy.orm import Session

from ..models import Media_type
from ..schemas import Media_typeCreateRequest


def add_(
    body: Media_typeCreateRequest,
    db_session: Session,
):
    Media_type_ = Media_type(
                            name=body.name,
                            note=body.note)
    db_session.add(Media_type_)

    try:
        db_session.flush()
        return Media_type_
    except Exception as ex:
        Get_Exceptions_details(ex)
