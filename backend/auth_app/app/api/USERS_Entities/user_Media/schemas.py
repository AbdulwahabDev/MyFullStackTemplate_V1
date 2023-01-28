from datetime import datetime
from pydantic import BaseModel


class User_MediaResponse(BaseModel):
    id: str
    user_id: str
    media_type_id: str
    updated :datetime
    name: str
    URL: str | None

    class Config:
        orm_mode = True

 
 

class User_MediaCreateRequest(BaseModel): 
    user_id: str
    media_type_id: str 
    name: str
    URL: str | None


class User_MediaUpdateRequest(BaseModel): 
    name: str
    URL: str 
