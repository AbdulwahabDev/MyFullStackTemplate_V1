from sqlalchemy import select 


from sqlalchemy.orm import Session  , Query
from ..models import user_UserType

from app.api.USERS_Entities.users.models import Users
from app.api.USERS_Entities.userType.models import UserType


def get_list_user_UsersType_(session: Session): 
    orm_query = (
                    session.query(
                                    Users.id.label("User_id"),
                                    Users.name.label("User_name"),
                                    UserType.name.label("UserType_name"), 
                                    user_UserType.updated,
                                    user_UserType.created,
                                    user_UserType.note,
                                ) 
                                .join(Users,   Users.id == user_UserType.user_id )
                                .join(UserType, UserType.id == user_UserType.usertype_id) 
                                .order_by(user_UserType.updated.desc())
                )
    suser_UserType  = session.execute(orm_query).all()
    return suser_UserType
