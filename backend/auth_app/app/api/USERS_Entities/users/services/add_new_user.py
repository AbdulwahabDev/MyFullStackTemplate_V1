from fastapi import HTTPException, status
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
    get_a_userType_by_id_(userType_id=body.UserType_id,db_session=db_session) 
    

    user = Users(
        username=body.username.lower(),
        password=hash_password(body.password),
        name=body.name,
        email=body.email.lower(),
    )
    db_session.add(user)

    try:
        db_session.flush()
        user_UsersTypeCreateRequest_ = user_UsersTypeCreateRequest(user_id=user.id,usertype_id=body.UserType_id,note='First usertype for this user ...')
        add_new_user_UsersType_(body=user_UsersTypeCreateRequest_,db_session=db_session)
        
        return user
    except IntegrityError as ex:
        if str(ex).startswith("(psycopg2.errors.ForeignKeyViolation)"):
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_ENTITY, "ForeignKeyViolation You Must Add Valid userstype_id!"
            )
        elif str(ex).startswith("(psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint"):
            raise HTTPException(status.HTTP_409_CONFLICT, str(ex).splitlines()[0])
        else:
            raise HTTPException(status.HTTP_502_BAD_GATEWAY, str(ex).splitlines()[0])
    except Exception as ex:
        print("Exception Name : ", ex.__class__.__name__)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(ex).splitlines()[0])
