from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    Username:str
    Fullname:str
    Password:str