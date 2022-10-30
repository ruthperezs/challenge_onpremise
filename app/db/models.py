from .database import Base
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.schema import ForeignKey


class hiredemployees(Base):
    __tablename__ = "hired_employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(Integer,ForeignKey("department_id",ondelete="CASCADE"))
    job_id = Column(Integer,ForeignKey("job_id",ondelete="CASCADE"))

class departments(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    department= Column(String)


class jobs(Base):
    __tablename__= "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job= Column(String)