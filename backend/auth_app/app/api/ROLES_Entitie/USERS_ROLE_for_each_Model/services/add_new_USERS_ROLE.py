from commons.exceptions import *

 
 
from sqlalchemy.orm import Session

from ..models import USERS_ROLE_for_each_Model as USERS_ROLE
from ..schemas import USERS_ROLE_for_each_Model_CreateRequest
 
def add_new_USERS_ROLE_(
    body: USERS_ROLE_for_each_Model_CreateRequest,
    db_session: Session,
):
    USERS_ROLE_ = USERS_ROLE( 
        user_id=body.user_id,
        model_id=body.model_id,
        role_id=body.role_id,
        note=body.note,
    )
    db_session.add(USERS_ROLE_)

    try:
        db_session.flush()
        return USERS_ROLE_  
    except Exception as ex:
        Get_Exceptions_details(ex)
         
