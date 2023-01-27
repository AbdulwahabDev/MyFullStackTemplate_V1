from sqlalchemy.orm import Session

from ..helpers import get_USERS_ROLE
from ..schemas import USERS_ROLE_for_each_Model_UpdateRequest


def update_a_USER_ROLE_by_id_(
    user_id: str,model_id: str,role_id: str,
    body: USERS_ROLE_for_each_Model_UpdateRequest,
    db_session: Session,
):
    USERS_ROLE_ = get_USERS_ROLE(
                                    user_id=user_id,
                                    model_id=model_id,
                                    role_id=role_id,
                                    db_session=db_session
                                 )
 
    USERS_ROLE_.note = body.note 

    return USERS_ROLE_
