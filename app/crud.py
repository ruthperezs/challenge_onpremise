from statistics import mode
from fastapi import APIRouter,Depends
from datetime import datetime, timezone
from db.database import get_db
from schemas import *
from sqlalchemy.orm import Session

from db import models


def get_hired_employees(db: Session):
    return db.query(models.hiredemployees).all()

def get_jobs(db: Session):
    return db.query(models.jobs).all()

def get_departments(db: Session):
    return db.query(models.departments).all()

def get_informe1(db: Session):
    return db.query(models.hiredemployees).all()

def get_informe2(db: Session):
    return db.query(models.hiredemployees).all()