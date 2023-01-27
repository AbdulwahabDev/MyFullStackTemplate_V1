from commons.exceptions import *
from sqlalchemy.orm import Session

from ..models import Role_Models
from ..schemas import Role_ModelsCreateRequest
 
def add_new_Role_Model_(
    body: Role_ModelsCreateRequest,
    db_session: Session,
):
    Role_Models_ = Role_Models( 
        name=body.name,
        note=body.note,
    )
    db_session.add(Role_Models_)

    try:
        db_session.flush()
        return Role_Models_
    except Exception as ex:
        Get_Exceptions_details(ex)
        
