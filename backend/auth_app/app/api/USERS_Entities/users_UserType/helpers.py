from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import user_UserType
from app.api.USERS_Entities.userType.models import UserType
from app.api.USERS_Entities.users.models import Users
from .models import user_UserType


# def get_user_UserType(usertype_id: str, user_id: str, db_session: Session) -> user_UserType:
#     stmt = select(user_UserType).where((user_UserType.usertype_id == usertype_id) & 
#                                         (user_UserType.user_id == user_id))
#     user_UserType_: user_UserType | None = db_session.execute(stmt).scalar_one_or_none()

#     if user_UserType_ is None:
#         raise HTTPException(status.HTTP_404_NOT_FOUND)

#     return user_UserType_



def get_user_UserType(usertype_id: str, user_id: str,db_session: Session): 
    orm_query = (
                    db_session.query(
                                    Users.id.label("User_id"),
                                    Users.name.label("User_name"),
                                    UserType.name.label("UserType_name"), 
                                    user_UserType.updated,
                                    user_UserType.created,
                                    user_UserType.note,
                                ) 
                                .join(Users,   Users.id == user_UserType.user_id )
                                .join(UserType, UserType.id == user_UserType.usertype_id) 
                                .where((user_UserType.usertype_id == usertype_id) & (user_UserType.user_id == user_id))
                )
    user_UserType_  = db_session.execute(orm_query).first()
    return user_UserType_