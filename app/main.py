from fastapi import FastAPI

from app.database.database import Base, engine
from app.routers.payroll import router as payroll_router
from app.routers.employee import router as employee_router
from app.routers.auth import router as auth_router
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(employee_router)
app.include_router(payroll_router)
app.include_router(auth_router)