from fastapi import FastAPI
from typing import Optional


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


@app.get("/blog/{id}/comments")  #there is anything given in the path and that is accepted here so this this could be the path parameter otherwise you are talking about obviously the query parameter 
def comments(id, limit=10):
    #fetch comments of blog with id = id
    return {'data': {'1', '2'}}
