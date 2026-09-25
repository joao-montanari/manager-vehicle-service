from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
from database_config import bd
from models import User

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {
        "message": "you access the default authentication router",
        "authenticated": False,
    }

@auth_router.post("/create_user")
async def create_user(email: str, password: str, name: str):
    Session = sessionmaker(bind=bd)
    session = Session()

    user = session.query(User).filter(User.email == email).first()
    if user:
        return {
            "message": "User already exists",
        }
    else:
        new_user = User(name, email, password)
        session.add(new_user)
        session.commit()
        return {
            "message": "User created successfully",
        }
        