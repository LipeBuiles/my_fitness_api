from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    user_name: str
    email: str
    state: str

    class Config:
        from_attributes = True