from commons.exceptions import *
from sqlalchemy.orm import Session

from ..models import User_Media
from ..schemas import User_MediaCreateRequest


def add_(
    body: User_MediaCreateRequest,
    db_session: Session,
):
    User_Media_ = User_Media(user_id=body.user_id,
                            media_type_id=body.media_type_id,
                            name=body.name,
                            URL=body.URL)


    db_session.add(User_Media_)

    try:
        db_session.flush()
        return User_Media_
    except Exception as ex:
        Get_Exceptions_details(ex)
