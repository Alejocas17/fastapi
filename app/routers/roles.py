from fastapi import HTTPException, status
from fastapi import FastAPI
from fastapi import APIRouter,Depends
from fastapi.responses import HTMLResponse, JSONResponse
from app.squemas import Role
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.models import Role as UserRole
from datetime import datetime
# from app.db.models import Use

from app.db import models


router = APIRouter(
    prefix="/roles",
    tags = ["CRUD_ROLES"],
)

############################### Endpoints for USER adn ROLES #############################


@router.get("/getAll",tags=['CRUD_ROLES'])
async def getAllRoles(db:Session=Depends(get_db)):
    data = db.query(models.Role).all()

    return data

@router.get("/getOne",tags=['CRUD_ROLES'])
async def getOne(id:int,db:Session=Depends(get_db)):
    record = db.query(models.Role).filter_by(id=id).first()
    if record != None:
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay Role con ese ID"
        ) 

@router.post("/insert",tags=['CRUD_ROLES'])
async def insertRole(role: Role, db:Session=Depends(get_db)):

    data = db.query(models.Role).all()
    
    response=[item for item in data if item.role_name == role.role_name]
    # print(user.name)
    
    if response==[]:
        # Users.append(user.dict())
        new_role = UserRole(
            roleName = role.role_name,
            description =  role.description,
            isActive = role.is_active,
            createdAt = datetime.now(),
            updatedAt = datetime.now()
        )
        db.add(new_role)
        db.commit()
        db.close()
        data = db.query(models.Role).all()
        return data
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un rol con ese nombre"
        )

@router.put("/update",tags=['CRUD_ROLES'])
def updateRole(role: Role,id:int,db:Session=Depends(get_db)):
    response = db.query(models.Role).filter_by(id=id)
    created_date = response.first().createdAt
    if response != None:

        new_role = UserRole(
            roleName = role.role_name,
            description =  role.description,
            isActive = role.is_active,
        )

        print(response.first().created_at)
        print(new_role.role_name)
        response.update({models.Role.roleName:new_role.roleName},synchronize_session = False)
        response.update({models.Role.description:new_role.description},synchronize_session = False)
        response.update({models.Role.isActive:new_role.isActive},synchronize_session = False)
        response.update({models.Role.updatedAt:new_role.updatedAt},synchronize_session = False)
        response.update({models.Role.createdAt:created_date},synchronize_session = False)
        db.commit()
        db.close()
        data = db.query(models.Role).all()

        return data
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay Role con ese ID"
        ) 
    

@router.delete("/delete",tags=['CRUD_ROLES'])
async def deleteRole(id:int,db:Session=Depends(get_db)):
    flag=True

    record = db.query(models.Role).filter_by(id=id).first()
    
    if record != None:
        db.delete(record)
        db.commit()
        flag = False
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Se ha eliminado el Rol"
        ) 
    if flag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay rol con ese ID"
        ) 

