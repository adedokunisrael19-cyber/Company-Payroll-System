from fastapi import FastAPI

from app.database.database import Base, engine
from app.routers.payroll import router as payroll_router
from app.routers.employee import router as employee_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Company Payroll System",
    description="Payroll management API",
)

app.include_router(employee_router)
app.include_router(payroll_router)
