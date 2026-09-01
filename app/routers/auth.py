from fastapi import APIRouter
from fastapi.params import Depends
from starlette import status
from starlette.middleware.sessions import Session

from app.database.database import get_db
from app.schemas.admin import AdminResponse, AdminCreate
from app.services.auth import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", response_model=AdminResponse, status_code=status.HTTP_201_CREATED)

def register(admin_data: AdminCreate, db:Session = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.register(admin_data)


@router.post("/login")
def login(admin_data: AdminCreate, db:Session = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.login(admin_data)


@router.post("/logout")
def logout():
    return {
        "message" : "logout sucessful"
    }