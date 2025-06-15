from sqlalchemy  import Column,Integer, String,Date,BigInteger
from .database import Base
class Patients(Base):
    _tablename_ =  "patients"
    id = Column(BigInteger, primary_key=True,index=True,autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    diagnosis = Column(String, nullable=False)
    gaurdian = Column(String, nullable=False)
    date = Column(Date, nullable=False)
