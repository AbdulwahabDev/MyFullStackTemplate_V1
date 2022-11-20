

from pathlib import Path
import os
 
class ProjectConfigClass():
 
    def Get_APP_NAME(): 
        return  os.environ.get('APP_NAME')   
        
    def Get_AUTH_APP_URL():
        return  os.environ.get('AUTH_APP_URL')
         
