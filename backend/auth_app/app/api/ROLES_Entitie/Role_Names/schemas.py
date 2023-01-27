from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Role_NamesResponse(BaseModel):
    role_id: str 
    name:str
    note: str
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True 


class Role_NamesCreateRequest(BaseModel): 
    name: str 
    note: str | None


class Role_NamesUpdateRequest(BaseModel):
    name: str | None
    note: str | None

 