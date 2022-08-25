from fastapi import FastAPI
from file import file_route
import uvicorn
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app=FastAPI()


app.include_router(file_route,prefix='/file')

IMAGE_ROOT='F:/Fast Api/fourth_project/images/'

FILE_ROOT='F:/Fast Api/fourth_project/files/'

@app.get("/")
def index_welcome():
     return {'welcome':'welcome to fastapi downloader'}

     
if __name__ == "__main__":
     uvicorn.run("main:app", host="0.0.0.0", port=9000,reload=True)