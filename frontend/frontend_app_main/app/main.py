

from starlette.staticfiles import StaticFiles
from pathlib import Path 

import os,sys
 

sys.path.append(os.path.abspath('frontend/'))  
sys.path.append(os.path.abspath('app/')) 

 

from app.config import set_up_main
from app.Views.Home.index import index_router
from app.Views.authentication.sign import sign_router
from app.Views.Profile.Proflie import Proflie_router
from app.Views.shared.shared import shared_router




app = set_up_main( 
    routers_modules=[ 
        shared_router,
        Proflie_router,
        index_router,
        sign_router,
        
        
    ],
)

app.mount('/dist', StaticFiles(directory=Path(__file__).resolve().parent.parent.joinpath('Template/dist')))    
