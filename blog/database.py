#read doc from https://fastapi.tiangolo.com/tutorial/sql-databases/

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db' #defining database URL 


engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread": False}) # creating engine

#Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()