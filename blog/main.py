from fastapi import FastAPI
from . import schemas, models
from .database import engine 
from sqlalchemy.orm import Session 

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)): #getting error
    return request


