from datetime import datetime
from pydantic import BaseModel


class User_PhoneResponse(BaseModel):
    id: str
    user_id: str
    updated :datetime
    phone: str
    note: str | None

    class Config:
        orm_mode = True



 

class User_PhoneCreateRequest(BaseModel): 
    user_id: str 
    phone: str
    note: str | None


class User_PhoneUpdateRequest(BaseModel): 
    phone: str | None
    note: str | None
