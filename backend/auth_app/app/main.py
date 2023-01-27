
import sys , os 
sys.path.append(os.path.abspath('backend/auth_app/'))  

from commons.main import set_up_main

from .api.routes_check import test_router
from .api.USERS_Entities.users.routes import users_router
from .api.USERS_Entities.userType.routes import userType_router
from .api.USERS_Entities.users_UserType.routes import user_usertype_router
from .api.USERS_Entities.routes import USERS_Entities_seeds_router

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
    ],
)
