from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patients management system API is running!"}

@app.get("/shubham")
def about():
    return {"msg": "A Fully functional patients management system API built using FastAPI and MongoDB."}


@app.get("/view")
def view():
    data = load_data()
    return   data  
   