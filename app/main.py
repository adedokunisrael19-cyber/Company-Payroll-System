from fastapi import FastAPI

from app.database.connection import Base, engine
from app.controllers.employee_controller import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)