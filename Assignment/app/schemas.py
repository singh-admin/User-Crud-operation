from typing import List, Union

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str

# Pydantic model for response
class UserResponse(BaseModel):
    id: int
    name: str
    message: str

class APIKeyCreate(BaseModel):
    name: str


