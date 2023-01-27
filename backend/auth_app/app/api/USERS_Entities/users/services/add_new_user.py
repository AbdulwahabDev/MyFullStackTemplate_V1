from fastapi import HTTPException, status
from commons.exceptions import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..helpers import hash_password
from ..models import Users
from ..schemas import UsersCreateRequest

from app.api.USERS_Entities.userType.services.get_a_userType_by_id import get_a_userType_by_id_

from app.api.USERS_Entities.users_UserType.schemas import user_UsersTypeCreateRequest
from app.api.USERS_Entities.users_UserType.services.add_new_user_UsersType import add_new_user_UsersType_


def add_new_user_(
    body: UsersCreateRequest,
    db_session: Session,
):
    
    # Cheack if user type found ... 
    get_a_userType_by_id = get_a_userType_by_id_(userType_id=body.UserType_id,db_session=db_session) 
    
    photo = body.photo if body.photo else 'assets/media/avatars/blank.png' 
    user = Users(
        username=body.username.lower(),
        password=hash_password(body.password),
        name=body.name,
        email=body.email.lower(),
        photo=photo
    )
    db_session.add(user)

    try:
        db_session.flush()
        user_UsersTypeCreateRequest_ = user_UsersTypeCreateRequest(user_id=user.id,usertype_id=body.UserType_id,note='First usertype for this user ...')
        add_new_user_UsersType_(body=user_UsersTypeCreateRequest_,
                                First_Time=True,
                                db_session=db_session)
        return user
    except Exception as ex:
        Get_Exceptions_details(ex)
