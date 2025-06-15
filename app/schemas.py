from pydantic import BaseModel
import DateTime import date as Date
class PatientBase(BaseModel):
    name    :   str = None 
    age     :   int=None
    gender  :   str=None
    contact :   str=None
    diagnosis:  str=None
    date    :   Date=Date.today()
    guardian:   str=None
class PatientCreate(PatientBase):
    pass
class Patient(PatientBase):
    id:int
    class Config:
        orm_mode=True
        from_attributes=True