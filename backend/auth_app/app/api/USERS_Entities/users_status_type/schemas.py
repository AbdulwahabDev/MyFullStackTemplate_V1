from pydantic import BaseModel


class Users_Status_typeResponse(BaseModel):
    id: str
    name: str
    note: str

    class Config:
        orm_mode = True


class Users_Status_typeCreateRequest(BaseModel):
    name: str
    note: str | None


