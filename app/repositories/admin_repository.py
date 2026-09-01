from sqlalchemy.orm import session, Session

from app.models.Admin import Admin
from app.schemas.admin import AdminCreate


class AdminRepository:
    def __init__(self, db:Session):
        self.db = db

    def create (self, admin_data: AdminCreate) -> Admin:
        admin = Admin(
            username=admin_data.username,
            email=admin_data.email,
            password=admin_data.password
        )

        self.db.add(admin)
        self.db.commit()
        self.db.refresh(admin)

        return admin

    def get_by_email(self, email:str) -> Admin | None:
        return( self.db.query(Admin).filter(Admin.email == email).first())

    def  get_by_username(self, username:str) -> Admin | None:
        return( self.db.query(Admin).filter(Admin.username == username).first())