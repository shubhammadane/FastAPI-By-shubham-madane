from fastapi import FastAPI, Path,HTTPException
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
   
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str= Path(..., description="The ID of the patient to retrieve",example="P001 ")):
    data = load_data()

    for patient in data["patients"]:
        if patient["id"] == patient_id:
            return patient

        raise HTTPException(status_code=404, detail="Patient not found")