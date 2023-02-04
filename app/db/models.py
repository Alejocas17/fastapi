from app.db.database import Base
from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    lastName = Column(String)
    address = Column(String)
    cellphone = Column(String)
    mail = Column(String)
    created_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)