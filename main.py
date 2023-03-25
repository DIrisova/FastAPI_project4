from fastapi import FastAPI


app = FastAPI()

@app.get("/")

def index():
    #return {'data': {'name': 'Dilobar'}}
    return {'data': 'blog list'}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get("/blog/{id}")
def show(id: int): #int is converting id to the integer. In case we want string we can simply use str instead of int
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id):
    #fetch comments of blog with id = id
    return {'data': {'1', '2'}}
