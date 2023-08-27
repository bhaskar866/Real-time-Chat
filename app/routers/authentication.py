# app/routers/authentication.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_session
from models.user import User
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register/")
def register(username: str, password: str, db: Session = Depends(get_session)):
    # Check if the username is already taken
    print("Check point")
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Hash the password
    hashed_password = pwd_context.hash(password)
    
    # Create the user in the database
    new_user = User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User registered successfully"}
