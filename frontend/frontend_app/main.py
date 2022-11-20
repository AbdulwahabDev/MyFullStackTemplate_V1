

from starlette.staticfiles import StaticFiles
from pathlib import Path 

import os,sys
 

sys.path.append(os.path.abspath('frontend/'))  
sys.path.append(os.path.abspath('frontend_app/')) 

 

from frontend_app.config import set_up_main
from frontend_app.Views.Home.index import index_router
from frontend_app.Views.authentication.sign import sign_router
from frontend_app.Views.Profile.Proflie import Proflie_router
from frontend_app.Views.shared.shared import shared_router
from frontend_app.Views.reports.visits.visits import visits_router



app = set_up_main( 
    routers_modules=[ 
        shared_router,
        Proflie_router,
        index_router,
        sign_router,
        visits_router
        
        
    ],
)

app.mount('/dist', StaticFiles(directory=Path(__file__).resolve().parent.parent.joinpath('Template/dist')))    
