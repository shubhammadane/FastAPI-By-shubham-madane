from fastapi import FastAPI, Path,HTTPException, Query
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



@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'),
    order: str = Query('asc', description='sort in asc or desc order')
):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order.lower() not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order.lower() == 'desc' else False

    sorted_data = sorted(
        data["patients"],   # ✅ FIX HERE
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data