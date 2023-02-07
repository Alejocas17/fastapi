from app.db.database import Base
from sqlalchemy import Column, Integer, DateTime, String, Boolean
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

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True,autoincrement=True)
    role_name = Column(String)
    description = Column(String)
    is_active = Column(Boolean)
    created_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    updated_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)


