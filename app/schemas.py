from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr = Field(..., description="Valid email address", example="user@email.com")
    username: str = Field(..., description="Username", example="jdoe")

class UserRead(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        orm_mode = True
