

from pathlib import Path
import os
 
class ProjectConfigClass():
  
    def Get_AUTH_JWT_KEY():
        return os.environ.get('AUTH_JWT_KEY')
         
    def Get_DB_HOST():
        return  os.environ.get('DB_HOST')
       
    def Get_DB_USER(): 
        return  os.environ.get('POSTGRES_USER')
        
    def Get_DB_PASSWORD():
        return  os.environ.get('POSTGRES_PASSWORD')
        
    def Get_DB_PORT():
        return  os.environ.get('DB_PORT') 

    def Get_AUTH_SALT():
        return  os.environ.get('AUTH_SALT') 

    def Get_HASH_ALGORITHM(): 
        return  os.environ.get('HASH_ALGORITHM') 

    def Get_ACCESS_TOKEN_EXPIRE_IN_SECONDS():
        return  os.environ.get('ACCESS_TOKEN_EXPIRE_IN_SECONDS')
    
    def Get_AUTH_APP_URL():
        return  os.environ.get('AUTH_APP_URL')
 
