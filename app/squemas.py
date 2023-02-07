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
    created_at: datetime = datetime.now()

class Role(BaseModel):
    id : Optional[int] = None
    role_name : str
    description : str
    is_active : bool
    updated_at : datetime = datetime.now()
    created_at : datetime = datetime.now()
