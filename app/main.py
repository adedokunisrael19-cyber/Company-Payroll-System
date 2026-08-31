from fastapi import FastAPI

from app.database.database import Base, engine
from app.routers.employee import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)