from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    Username:str
    Fullname:str
    Password:str
    IsAdmin:Optional[int] = 0
    
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    Username:str
    Password:str
    
    class Config:
        orm_mode = True