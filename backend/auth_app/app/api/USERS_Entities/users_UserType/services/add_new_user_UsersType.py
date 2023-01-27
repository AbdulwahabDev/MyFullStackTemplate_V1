from commons.exceptions import * 

from sqlalchemy.orm import Session

from ..models import user_UserType
from ..schemas import user_UsersTypeCreateRequest

from ..services import get_a_user_UsersType_by_id

# users_UserType


def add_new_user_UsersType_(
    body: user_UsersTypeCreateRequest,
    db_session: Session,
    First_Time:bool = False
):
    user_UserType_ = user_UserType(
        user_id=body.user_id,
        usertype_id=body.usertype_id,
        note=body.note,
    )
    db_session.add(user_UserType_)

    try:
        db_session.flush()
        
        if First_Time: 
            return user_UserType_
        else:  
            user_UserType_with_names = get_a_user_UsersType_by_id.get_a_users_UserType_by_id_(user_id=body.user_id,
                                                                            userType_id=body.usertype_id,
                                                                            db_session=db_session)
            return user_UserType_with_names
         
    except Exception as ex:
        Get_Exceptions_details(ex) 

 
