from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///./bookstore.db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

base = declarative_base()

Session_local =sessionmaker(bind=engine,autoflush=False,autocommit=False)