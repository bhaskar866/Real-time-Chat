import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()
from dotenv import load_dotenv
load_dotenv()

db_username = os.environ.get("DATA_BASE_USERNAME")
db_password = os.environ.get("DATA_BASE_PASSWORD")
db_host = os.environ.get("DATA_BASE_HOSTNAME")
db_name = os.environ.get("DATA_BASE_NAME")
jwt_secret = os.getenv("JWT_SECRET_KEY")



DATABASE_URL = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_host}/{db_name}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

