from sqlalchemy import select


from sqlalchemy.orm import Session
from ..models import USERS_ROLE_for_each_Model as USERS_ROLE
from app.api.ROLES_Entitie.Role_Models.models import Role_Models
from app.api.ROLES_Entitie.Role_Names.models import Role_Names
from app.api.USERS_Entities.users.models import Users


def get_list_USERS_ROLE_(session: Session): 
    orm_query = (
                    session.query(
                                    USERS_ROLE.log_id,
                                    
                                    Users.name.label("User_name"),
                                    USERS_ROLE.user_id,
                                    Role_Models.name.label("Model_name"),
                                    USERS_ROLE.model_id,
                                    Role_Names.name.label("Role_name"),
                                    USERS_ROLE.role_id,
                                    USERS_ROLE.created,
                                    USERS_ROLE.note,
                                ) 
                                .join(Users,   Users.id == USERS_ROLE.user_id )
                                .join(Role_Models,   Role_Models.model_id == USERS_ROLE.model_id )
                                .join(Role_Names,   Role_Names.role_id == USERS_ROLE.role_id ) 
                                .order_by(USERS_ROLE.updated.desc())
                )
    list_USERS_ROLE_  = session.execute(orm_query).all()
    return list_USERS_ROLE_
