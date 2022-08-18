import imp
from fastapi import FastAPI

# creating app as instance of FastAPI
app = FastAPI()

# setting our default get request for the "/" url as a welcome message to test uvicorn
@app.get("/")
def root():
    return {"message": "Welcome to my api!!!"}
    