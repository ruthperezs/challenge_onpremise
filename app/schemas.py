from datetime import date
from pydantic import BaseModel

class hired(BaseModel):
    id: int
    name: str
    datatime: str
    department_id: int
    job_id: int

    class Config:
        orm_mode = True


class departaments(BaseModel):
    id: int
    departament: str

    class Config:
        orm_mode = True

class job(BaseModel):
    id: int
    job: str

    class Config:
        orm_mode = True
