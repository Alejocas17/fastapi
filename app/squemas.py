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