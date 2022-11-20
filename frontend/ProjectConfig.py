

import json
from pathlib import Path
import os
 
class ProjectConfigClass():
 
    def Get_APP_NAME(): 
        return  os.environ.get('APP_NAME')  

    def Get_AUTH_JWT_KEY():
        return os.environ.get('AUTH_JWT_KEY')

    def Get_AUTH_SALT():
        return  os.environ.get('AUTH_SALT') 

    def Get_HASH_ALGORITHM(): 
        return  os.environ.get('HASH_ALGORITHM') 

    def Get_ACCESS_TOKEN_EXPIRE_IN_SECONDS():
        return  os.environ.get('ACCESS_TOKEN_EXPIRE_IN_SECONDS')
    
    def Get_AUTH_APP_URL():
        return  os.environ.get('AUTH_APP_URL')
         
