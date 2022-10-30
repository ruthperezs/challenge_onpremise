from datetime import datetime
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
  id:int
  name:str
  apellido:str
  direccion:Optional[str]
  telefono:int
  creacion_user:datetime=datetime.now()


app = FastAPI()
usuarios = []
@app.get("/hiredemployees")
def obtener_hiredemployees():
  return {"mensaje": "Bienvenido a la API Challenge :) "}

@app.get("/departments")
def obtener_departments():
  print("req1")
  return True

@app.get("/jobs")
def obtener_jobs():
  print("req2")
  return True

@app.get("/challenge2/informe1")
def informe1():
  print("req2")
  return True

@app.get("/challenge2/informe2")
def informe2():
  print("req2")
  return True

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
