from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hi Shubham, Welcome to FastAPI!"}

@app.get("/shubham")
def greet():
    return {"msg": "Hello Shubham, How are you?"}