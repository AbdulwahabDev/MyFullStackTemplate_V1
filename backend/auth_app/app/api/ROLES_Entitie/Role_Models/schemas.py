from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Role_ModelsResponse(BaseModel):
    model_id: str 
    name:str
    note: str
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True 


class Role_ModelsCreateRequest(BaseModel): 
    name: str 
    note: str | None


class Role_ModelsUpdateRequest(BaseModel):
    name: str | None
    note: str | None

 