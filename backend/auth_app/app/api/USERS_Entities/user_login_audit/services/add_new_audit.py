from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..models import User_Login_Audit


def logIn_audit_(
    user_id: str,
    user_name: str,
    name: str,
    db_session: Session,
):
    user_Login_Audit = User_Login_Audit(user_id=user_id, user_name=user_name, name=name, note="LogIn")
    db_session.add(user_Login_Audit)

    try:
        db_session.flush()
        return "pass"
    except Exception as ex:
        print("Exception Name : ", ex.__class__.__name__)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(ex).splitlines()[0])


def logOut_audit_(
    user_id: str,
    user_name: str,
    name: str,
    db_session: Session,
):
    user_Login_Audit = User_Login_Audit(user_id=user_id, user_name=user_name, name=name, note="logOut")
    db_session.add(user_Login_Audit)

    try:
        db_session.flush()
        return "pass"
    except Exception as ex:
        print("Exception Name : ", ex.__class__.__name__)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(ex).splitlines()[0])
