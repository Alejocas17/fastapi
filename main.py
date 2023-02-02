from fastapi import HTTPException, status
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional


import sentry_sdk


sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

#temporary DataBase

Users = [
    {
        "id": 1,
        "name": "Alejandro",
        "lastname": "Castillo",
        "cellphone": "3168213658",
        "address": "ciudadela comfandi"

    },
     {
        "id": 2,
        "name": "Edward",
        "lastname": "Montaño",
        "cellphone": "123456",
        "address": "Cali"

    },
     {
        "id": 3,
        "name": "David",
        "lastname": "Franco",
        "cellphone": "1230982",
        "address": "jamundi"

    }
]

app = FastAPI()

class User(BaseModel):
    id : Optional[int] = None
    name : str
    lastname: str
    cellphone: str
    address: str

############################### Endpoints for USER #############################


#Endpoint for Get one user filtered by id
@app.get("/getOne/{id}",tags=['CRUD'])
async def getOne(id:int):
    response = [item for item in Users if item["id"] == id]
    if response != []:
        return JSONResponse(content=response)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay usuario con ese ID"
        ) 


#Endpoint for Get all of the users
@app.get("/getAll",tags=['CRUD'])
async def getAll():
    return JSONResponse(content=Users)

#Endpoint for delete one user by id
@app.delete("/deleteUser/{id}",tags=['CRUD'])
async def deleteUser(id:int):
    flag=True
    for item in Users:
        if item["id"] == id:
            Users.remove(item)
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

@app.post("/insertUser",tags=['CRUD'])
async def insertUser(user: User):
    response=[item for item in Users if item["id"] == user.id]

    if response == []:
        Users.append(user.dict())
        print("Se añadió el usuario")
        return JSONResponse(content=Users)
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un usuario con ese ID"
        ) 





############################### Endpoints for USER adn ROLES #############################


@app.get("/getAllRoles",tags=['CRUD_ROLES'])
def getAllRoles():
    pass

@app.get("/getOneRole",tags=['CRUD_ROLES'])
def getOneRole():
    pass

@app.post("/createUserRole",tags=['CRUD_ROLES'])
def createUserRole():
    pass

@app.put("/updateUserRole",tags=['CRUD_ROLES'])
def updateUserRole():
    pass

@app.delete("/deleteUserRole",tags=['CRUD_ROLES'])
def deleteUserRole():
    pass

