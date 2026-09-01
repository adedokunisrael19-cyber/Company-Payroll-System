from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.admin_repository import AdminRepository
from app.schemas.admin import AdminCreate


class AuthService:
    def __init__(self,db: Session):
        self.admin_repository = AdminRepository(db)

    def register(self, admin_data: AdminCreate):
        existing_email = self.admin_repository.get_by_email(admin_data.email)
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")
        existing_username = self.admin_repository.get_by_username(admin_data.username)

        if existing_username:
            raise HTTPException(status_code=400, detail="Username already taken")
        return self.admin_repository.create(admin_data)


    def login(self, login_data: AdminCreate):
        admin = self.admin_repository.get_by_email(login_data.email)

        if not admin:
            raise HTTPException(status_code=400, detail="invalid email or password")
        if admin.password != login_data.password:
            raise HTTPException(status_code=400, detail="invalid email or password")
        