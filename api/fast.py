from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from bucketapi.bucket import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}


@app.get("/data")
def databucket(filename, extension='csv', nrows=None):

    filename = f"{filename}.{extension}"
    print('XXXXXXXXXXXX')
    print(filename)
    print('XXXXXXXXXXXX')

    if nrows:
        nrows = int(nrows)

    data = Getbucket().get(filename=filename, nrows=nrows)

    return data

@app.post("/data")
def data(filename, data):

    res = Getdata().post(filename=filename, data=data)

    return res
