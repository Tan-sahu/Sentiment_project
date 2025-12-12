from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

# Schema for Token Response
class Token(BaseModel):
    access_token: str
    token_type: str

# Schema for Token Data (payload)
class TokenData(BaseModel):
    email: str | None = None