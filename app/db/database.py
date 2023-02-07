from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



Base = declarative_base()

# aquí puedes agregar tus modelos de SQLAlchemy

engine = create_engine("postgresql://postgres:iI3EhBpxswPav5ZwxrCw@containers-us-west-50.railway.app:7449/railway")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


