from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class user_UsersTypeResponse(BaseModel):
    User_id: str
    User_name: str
    UserType_name: str 
    updated: datetime
    note: str

    class Config:
        orm_mode = True


class user_UsersTypeCreateRequest(BaseModel):
    usertype_id: str
    user_id: str
    note: str


class user_UsersTypeUpdateRequest(BaseModel):
    note: str


# userstype_id = sa.Column(sa.String, primary_key=True)
# users_id = sa.Column(sa.String, primary_key=True)
# note = sa.Column(sa.String)
# created = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
# updated = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
