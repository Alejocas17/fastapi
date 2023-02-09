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
    createdAt = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    updatedAt = Column(DateTime,default=datetime.now,onupdate=datetime.now)

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True,autoincrement=True)
    roleName = Column(String)
    description = Column(String)
    isActive = Column(Boolean,default=True,nullable=True)
    createdAt = Column(DateTime,default=datetime.now,onupdate=datetime.now, nullable=True)
    updatedAt = Column(DateTime,default=datetime.now,onupdate=datetime.now, nullable=True)


