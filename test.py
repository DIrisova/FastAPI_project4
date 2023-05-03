
from fastapi import FastAPI, Body
from typing import List
from google.cloud import storage


app = FastAPI()


@app.get('/')
def index():
    return "Hello"


@app.post('/api/v1/scrape')
def scrape(files: List[str]=Body(..., embed=True)): 

    bucket_name = "client_network"
    prefix = "staging"


    client = storage.Client() #creating connection
    bucket = client.bucket(bucket_name) 

    blobs = bucket.list_blobs(prefix=prefix) 
    list_of_files = list(blobs) 
    file_names = []  #empty list for storing the file names

    for blob in list_of_files:
        file_names.append(blob.name) 

    for f in files:
        file_index = file_names.index(f)

        strBlob = list_of_files[file_index].download_as_string()  
        print(strBlob)

    return {"message": "success"}



   
