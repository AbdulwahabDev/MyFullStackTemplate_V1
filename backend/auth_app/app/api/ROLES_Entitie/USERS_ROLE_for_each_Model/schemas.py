from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class USERS_ROLE_for_each_Model_Response(BaseModel):
    log_id: str 
    User_name:str
    user_id: str 
    Model_name :str
    model_id: str 
    Role_name:str
    role_id: str  
    created: datetime 
    note: str 

    class Config:
        orm_mode = True 


class USERS_ROLE_for_each_Model_CreateRequest(BaseModel): 
    user_id: str 
    model_id: str 
    role_id: str 
    note: str | None


class USERS_ROLE_for_each_Model_UpdateRequest(BaseModel): 
    note: str 
 