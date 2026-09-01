from pydantic import BaseModel
from pydantic.v1 import EmailStr


class AdminCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class AdminLogin(BaseModel):
    email: EmailStr
    password: str

class AdminResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

    # i added this for the front end for accesing protected endpoint