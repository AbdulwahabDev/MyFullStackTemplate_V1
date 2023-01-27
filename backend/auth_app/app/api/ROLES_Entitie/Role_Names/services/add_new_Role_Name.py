from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from commons.exceptions import *

from ..models import Role_Names
from ..schemas import Role_NamesCreateRequest
 
def add_new_Role_Name_(
    body: Role_NamesCreateRequest,
    db_session: Session,
):
    Role_Names_ = Role_Names( 
        name=body.name,
        note=body.note,
    )
    db_session.add(Role_Names_)

    try:
        db_session.flush()
        return Role_Names_
    except Exception as ex:
        Get_Exceptions_details(ex)
