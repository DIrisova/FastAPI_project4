from fastapi import FastAPI, Depends, status, Response, HTTPException  
from . import schemas, models
from .database import engine, SessionLocal  
from sqlalchemy.orm import Session 

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
# Store blog to database
@app.post('/blog', status_code=status.HTTP_201_CREATED) 
def create(request: schemas.Blog, db: Session = Depends(get_db)): #requeat means whatever we pass from the swager
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'status': 'deleted'}


#update
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this id {id} is not found")
    #blog.update(request)
    data = dict(request)  # Convert request object to dictionary
    blog.update(data)
    db.commit()
    return 'updated'


@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog

#Status code
@app.get('/blog/{id}', status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with this id {id} is not available"}
    
    return blog 
         







