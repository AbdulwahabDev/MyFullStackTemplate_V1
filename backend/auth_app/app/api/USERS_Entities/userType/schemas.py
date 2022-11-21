from pydantic import BaseModel


class UserTypeResponse(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class UserTypeCreateRequest(BaseModel):
    name: str


class UserTypeUpdateRequest(BaseModel):
    name: str
