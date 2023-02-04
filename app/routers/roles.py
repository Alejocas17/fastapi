from main import app

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

