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
@app.get("/ruta1")
def ruta1():
  return {"mensaje": "Bienvenido a la API Challenge :) "}

@app.get("/requirement1")
def requirement1():
  print("req1")
  return True

@app.get("/requirement2")
def requirement2():
  print("req2")
  return True

@app.post("/test")
def test():
  
  print("AQUI")
  return True





if __name__ == "__main__":
    uvicorn.run("main:app",port=8000,reload=True)
