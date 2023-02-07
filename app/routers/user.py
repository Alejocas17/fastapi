from fastapi import HTTPException, status
from fastapi import FastAPI
from fastapi import APIRouter,Depends
from fastapi.responses import HTMLResponse, JSONResponse
from app.squemas import User
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.models import User as UserModel
# from app.db.models import Use

from app.db import models
# from main import app

##Router creation

router = APIRouter(
    prefix="/user",
    tags = ["CRUD"],
)

# Users = []

############################### Endpoints for USER #############################


#Endpoint for Get one user filtered by id
@router.get("/getOne/{id}",tags=['CRUD'])
async def getOne(id:int,db:Session=Depends(get_db)):
    record = db.query(models.User).filter_by(id=id).first()
    if record != None:
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay usuario con ese ID"
        ) 


#Endpoint for Get all of the users
@router.get("/getAll",tags=['CRUD'])
async def getAll(db:Session=Depends(get_db)):

    data = db.query(models.User).all()

    return data

#Endpoint for delete one user by id
@router.delete("/delete/{id}",tags=['CRUD'])
async def deleteUser(id:int,db:Session=Depends(get_db)):
    flag=True

    record = db.query(models.User).filter_by(id=id).first()
    
    if record != None:
        db.delete(record)
        db.commit()
        flag = False
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Se ha eliminado el usuario"
        ) 
    if flag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay usuario con ese ID"
        ) 

#Endpoint for insert new user

@router.post("/insert",tags=['CRUD'])
async def insertUser(user: User, db:Session=Depends(get_db)):

    data = db.query(models.User).all()
    
    response=[item for item in data if item.mail == user.mail]
    print(user.name)
    
    if response==[]:
        # Users.append(user.dict())
        new_user = UserModel(
            name = user.name,
            lastName =  user.lastName,
            cellphone = user.cellphone,
            address = user.address,
            mail = user.mail
        )
        db.add(new_user)
        db.commit()
        db.close()
        data = db.query(models.User).all()
        return data
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un usuario con ese correo"
        ) 


