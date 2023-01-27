
from commons.exceptions import *
from app.common.dependencies import db_session
from fastapi import APIRouter


USERS_Entities_seeds_router = APIRouter(prefix="/USERS_Entities_seeds", tags=["USERS_Entities_seeds"])


@USERS_Entities_seeds_router.get("")
def create_USERS_Entities_seeds(UserName: str, Paswword: str, db_session=db_session):
    """
    
    دالة تستخدم فقط في بداية البرنامج لإضافة البيانات الأساسيه لإستخددام النظام
    الخاصه لجداول المستخدمين

    """
    
    if UserName.lower() != "admin" or Paswword != "123456":
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "HTTP_401_UNAUTHORIZED")

    try: 
        user , usersType_name , status_name= create_user(db_session)
        return {
            "status": "Done :) Add First user in THE SYSTEM ! ",
            "id": user.id,
            "name": user.name,
            "username": user.username,
            "usersType": usersType_name,
            "status":status_name
        }
    except Exception as ex:
        Get_Exceptions_details(ex)

def create_all_status(db_session):
    from app.api.USERS_Entities.users_status_type.routes import add_
    from app.api.USERS_Entities.users_status_type.schemas import Users_Status_typeCreateRequest

    New_Status_ = add_(
        body=Users_Status_typeCreateRequest(name="New",note=""),
        db_session=db_session,
    )

    Available_Status_ = add_(
        body=Users_Status_typeCreateRequest(name="Available",note=""),
        db_session=db_session,
    )
    offline_Status_ = add_(
        body=Users_Status_typeCreateRequest(name="Offline",note=""),
        db_session=db_session,
    )
    busy_Status_ = add_(
        body=Users_Status_typeCreateRequest(name="Busy",note=""),
        db_session=db_session,
    )
    Apper_Status_ = add_(
        body=Users_Status_typeCreateRequest(name="Apper offline",note=""),
        db_session=db_session,
    )
    
    return New_Status_

def create_user_types(db_session):
    from app.api.USERS_Entities.userType.services.add_new_user_type import add_new_user_type_
    from app.api.USERS_Entities.userType.schemas import UserTypeCreateRequest

    usersType = add_new_user_type_(
        body=UserTypeCreateRequest(name="normal"),
        db_session=db_session,
    )

    Project_Owner_usersType = add_new_user_type_(
        body=UserTypeCreateRequest(name="Project_Owner"),
        db_session=db_session,
    )

    return Project_Owner_usersType





def create_user(db_session):
    
    from app.api.USERS_Entities.users.helpers import get_user
    CheckIFProjectOwnerAddedBefore = get_user(username="admin", db_session=db_session,First_Run_System=True)
    if CheckIFProjectOwnerAddedBefore:
        raise HTTPException(status.HTTP_226_IM_USED, "HTTP_226_IM_USED No Need to Do it Again !! ")




    usersType = create_user_types(db_session) # add_new_user_type_
    New_status = create_all_status(db_session) # create all status

    from app.api.USERS_Entities.users.services.add_new_user import add_new_user_
    from app.api.USERS_Entities.users.schemas import UsersCreateRequest

    usersCreateRequest = UsersCreateRequest(
        email="dev.abdulwahab@gmail.com",
        name="SITE ADMIN",
        username="admin",
        password="123456",
        UserType_id=usersType.id,
        status_id=New_status.id
    )
    user = add_new_user_(body=usersCreateRequest, db_session=db_session)

    return user , usersType.name , New_status.name
        



