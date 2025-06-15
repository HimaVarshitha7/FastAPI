from . import models,schemas,database
from fastapi import FastAPI, status, Depends
from .database import get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI("HealthCare_API")

@app.post("/patients",response_model = schemas.Patient,status_code=status.HTTP_201_CREATED)

def create_patient(patient:schemas.PatientCreate, db:Session = Depends(get_db)):
    db_Patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@app.get("/patients/{patient_id}",response_model=schemas.Patient,status_code=status.HTTP_200_Ok)
def get_patient(patient_id:int, db:Session = Depends(get_db)):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    return db_patient

