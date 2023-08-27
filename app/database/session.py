from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# app/database/sessions.py

from sqlalchemy.orm import Session


DATABASE_URL = "mysql+mysqlconnector://root:123456@localhost:3306/chatappdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

