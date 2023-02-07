from pydantic import BaseModel
from typing import Optional
from datetime import datetime
# from app.db.models import User

class User(BaseModel):

    id : Optional[int] = None
    name : str
    lastName: str
    cellphone: str
    address: str
    mail: str
    createdAt: datetime = datetime.now()
    updatedAt: datetime = datetime.now()

class Role(BaseModel):
    id : Optional[int] = None
    roleName : str
    description : str
    isActive : bool
    updatedAt : datetime = datetime.now()
    createdAt : datetime = datetime.now()
