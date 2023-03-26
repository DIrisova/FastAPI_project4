from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/blog")
def index(limit=10, published: bool=True, sort: Optional[str]=None):
    #return {'data': {'name': 'Dilobar'}}
    if published:
        return {'data': f'{limit} blogs lists'}
    else:
        return {'data': f'{limit} lists'}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get("/blog/{id}")
def show(id: int): #int is converting id to the integer. In case we want string we can simply use str instead of int
    return {'data': id}


@app.get("/blog/{id}/comments")  #there is anything given in the path and that is accepted here so this this could be the path parameter otherwise you are talking about the query parameter 
def comments(id, limit=10):
    #fetch comments of blog with id = id
    #return limit
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'success 200 yahoo title as {request.title}'}












