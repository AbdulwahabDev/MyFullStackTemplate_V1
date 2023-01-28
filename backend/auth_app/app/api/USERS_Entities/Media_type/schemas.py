from datetime import datetime
from pydantic import BaseModel


class Media_typeResponse(BaseModel):
    id: str  
    name: str
    note: str | None

    class Config:
        orm_mode = True



 

class Media_typeCreateRequest(BaseModel):  
    name: str
    note: str | None


class Media_typeUpdateRequest(BaseModel): 
    name: str | None
    note: str | None
