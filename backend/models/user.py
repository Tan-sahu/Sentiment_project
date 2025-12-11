from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

# Helper to map MongoDB's _id (ObjectId) to a string
PyObjectId = Annotated[str, BeforeValidator(str)]

class UserDB(BaseModel) :
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str
    email: EmailStr
    hashed_password : str
    
    class Config:
        populate_by_name = True
