
import sys , os 
sys.path.append(os.path.abspath('backend/auth_app/'))  

from commons.main import set_up_main

from .api.routes_check import test_router
from .api.USERS_Entities.users.routes import users_router
from .api.USERS_Entities.userType.routes import userType_router
from .api.USERS_Entities.users_UserType.routes import user_usertype_router
from .api.USERS_Entities.routes import USERS_Entities_seeds_router 

from .api.ROLES_Entitie.Role_Models.routes import role_models_router
from .api.ROLES_Entitie.Role_Names.routes import role_names_router
from .api.ROLES_Entitie.USERS_ROLE_for_each_Model.routes import users_role_router

from .config import config

app = set_up_main(
    config,
    routers_modules=[
        test_router,
        # USERS_Entities router start ---- 
        users_router,
        userType_router,
        user_usertype_router,
        USERS_Entities_seeds_router,
        # USERS_Entities  router start ---- 

        # ROLES_Entitie router start ---- 
        role_models_router,
        role_names_router,
        users_role_router,
        # ROLES_Entitie  router end ---- 
    ],
)
