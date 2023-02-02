from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



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
def getOne(id:int):
    return [item for item in Users if item["id"] == id]


#Endpoint for Get all of the users
@app.get("/getAll",tags=['CRUD'])
def getAll():
    return Users

#Endpoint for delete one user by id
@app.delete("/deleteUser/{id}",tags=['CRUD'])
def deleteUser(id:int):
    for item in Users:
        if item["id"] == id:
            Users.remove(item)
    return Users

#Endpoint for insert new user

@app.post("/insertUser",tags=['CRUD'])
def insertUser(user: User):

    Users.append(user.dict())
    return Users




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

