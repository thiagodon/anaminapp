from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router
from app.database import db, client
from app import config

app = FastAPI()

origins = [
    config.CLIENT_ORIGIN
]

@app.on_event('startup')
def startup_db_client():
    app.db = db

@app.on_event('shutdown')
def shutdown_db_client():
    client.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}