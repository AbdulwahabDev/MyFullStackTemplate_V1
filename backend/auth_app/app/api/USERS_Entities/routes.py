from fastapi import HTTPException, status

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

    from app.api.USERS_Entities.users.helpers import get_user

    CheckIFProjectOwnerAddedBefore = get_user(username="admin", db_session=db_session)

    if CheckIFProjectOwnerAddedBefore:
        raise HTTPException(status.HTTP_226_IM_USED, "HTTP_226_IM_USED No Need to Do it Again !! ")
    try:
        if True:  # add_new_user_type_

            from app.api.USERS_Entities.userType.services.add_new_user_type import add_new_user_type_
            from app.api.USERS_Entities.userType.schemas import UserTypeCreateRequest

            usersType = add_new_user_type_(
                body=UserTypeCreateRequest(name="Project_Owner"),
                db_session=db_session,
            )
            if True:  # add_new_user_

                from app.api.USERS_Entities.users.services.add_new_user import add_new_user_
                from app.api.USERS_Entities.users.schemas import UsersCreateRequest

                usersCreateRequest = UsersCreateRequest(
                    email="dev.abdulwahab@gmail.com",
                    name="SITE ADMIN",
                    password="admin",
                    username="123456",
                    UserType_id=usersType.id
                )
                user = add_new_user_(body=usersCreateRequest, db_session=db_session)

                return {
                    "status": "Done :) Add First user in THE SYSTEM ! ",
                    "id": user.id,
                    "name": user.name,
                    "username": user.username,
                    "usersType": usersType.name,
                }

    except Exception as ex:
        print(str(ex))
        # I should make it better later ... such from sqlalchemy.exc import IntegrityError
        # except IntegrityError:  etc ...
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "HTTP_500_INTERNAL_SERVER_ERROR")
