from datetime import datetime
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional,List
from datetime import datetime
from fastapi import Depends,Request
from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import *
from db.models import hiredemployees,departments,jobs
from db.database import SessionLocal,engine,get_db,Base
import crud
import backup

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/hiredemployees")
def obtener_hiredemployees(request: Request,db: Session = Depends(get_db)):
  data = crud.get_hired_employees(db)
  return data

@app.get("/departments")
def obtener_departments(request: Request,db: Session = Depends(get_db)):
  depart = crud.get_departments(db)
  return depart

@app.get("/jobs")
def obtener_jobs(request: Request,db: Session = Depends(get_db)):
  jobss= crud.get_jobs(db)
  return jobss

@app.get("/challenge2/informe1")
def informe1(request: Request,db: Session = Depends(get_db)):
  inf1 = crud.get_informe1(db)
  return inf1

@app.get("/challenge2/informe2")
def informe2(request: Request,db: Session = Depends(get_db)):
  inf2 = crud.get_informe2(db)
  return inf2

@app.get("/backup/h_empl")
def backup(request: Request,db: Session = Depends(get_db)):
  back = backup.do_backup1(db)
  return back

@app.get("/backup/job")
def backup(request: Request,db: Session = Depends(get_db)):
  back = backup.do_backup3(db)
  return back

@app.get("/backup/dep")
def backup(request: Request,db: Session = Depends(get_db)):
  back = backup.do_backup2(db)
  return back

@app.post("/batch/hiredemployees")
async def b_hiredemployees():
  
  print("AQUI")
  return True

@app.post("/batch/departments")
async def b_departments():
  
  print("AQUI")
  return True

@app.post("/batch/jobs")
async def b_jobs():
  
  print("AQUI")
  return True





if __name__ == "__main__":
    uvicorn.run("main:app",port=8000,reload=True)
