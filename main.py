from fastapi import HTTPException, status
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from app.squemas import User
import uvicorn
import sentry_sdk
from app.routers.user import router
from app.db.database import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

#temporary DataBase

# Users = [
#     {
#         "id": 1,
#         "name": "Alejandro",
#         "lastname": "Castillo",
#         "cellphone": "3168213658",
#         "address": "ciudadela comfandi"

#     },
#      {
#         "id": 2,
#         "name": "Edward",
#         "lastname": "Montaño",
#         "cellphone": "123456",
#         "address": "Cali"

#     },
#      {
#         "id": 3,
#         "name": "David",
#         "lastname": "Franco",
#         "cellphone": "1230982",
#         "address": "jamundi"

#     }
# ]

app = FastAPI()

app.include_router(router)

if __name__=='__main__':
    uvicorn.run("main:app",port=8000,reload=True,host="localhost")
