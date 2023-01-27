from typing import Optional
from pydantic import BaseModel
class UsersLoginRequest(BaseModel):
    username: str
    password: str

class UsersResponse(BaseModel):
    id: str
    username: str
    # password: str
    name: str
    email: str
    is_active: Optional[bool]
    # is_online: Optional[bool]
    photo: str

    class Config:
        orm_mode = True


class UsersLoginResponse(BaseModel):
    access_token: str


class UsersCreateRequest(BaseModel):
    username: str
    password: str
    name: str
    email: str
    is_active: Optional[bool]
    UserType_id: str
    photo: str | None





class UserUpdateRequest(BaseModel):
    name: str | None
    email: str | None
    photo: str | None
