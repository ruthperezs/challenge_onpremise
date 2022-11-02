from statistics import mode
from unittest import result
from fastapi import APIRouter,Depends
from datetime import datetime, timezone
from db.database import get_db
from schemas import *
from sqlalchemy.orm import Session
from sqlalchemy import text
from db.database import SessionLocal,engine,get_db,Base

from db import models


def get_hired_employees(db: Session):
    return db.query(models.hiredemployees).all()

def get_jobs(db: Session):
    return db.query(models.jobs).all()

def get_departments(db: Session):
    return db.query(models.departments).all()

def get_informe1(db: Session):
    sql= text('''SELECT department,job,sum(case when mes in (1,2,3) then 1 else 0 end) AS "Q1",
                sum(case when mes in (4,5,6) then 1 else 0 end) AS "Q2",
                sum(case when mes in (7,8,9) then 1 else 0 end) AS "Q3",
                sum(case when mes in (10,11,12) then 1 else 0 end) AS "Q4"
                FROM
                    (select A.id as emplo_id,B.department as department,C.job as job,A.datetime, 
                        cast(substring(A.datetime,6,2) as integer) as mes
                    from hired_employees as A 
                    join departments B on cast(A.department_id as int)=cast(B.id as int)
                    join jobs C on A.job_id=C.id
                    WHERE substring(A.datetime,1,4)='2021') TT 
                GROUP BY department,job
                ORDER BY department,job asc''')
    results = engine.execute(sql).fetchall()
    return results

def get_informe2(db: Session):
    sql2= text('''SELECT A.department_id as id,B.department,count(*) AS hired
                FROM hired_employees A
                join departments B on cast(A.department_id as int)=cast(B.id as int)
                WHERE substring(A.datetime,1,4)='2021'
                GROUP BY department_id,department
                HAVING count(*)>
	                (SELECT avg(TOTAL) as media 
	                FROM (select COUNT(department_id) as TOTAL from hired_employees A
	                join departments B on cast(A.department_id as int)=cast(B.id as int)
	                where substring(A.datetime,1,4)='2021' group by department_id) AA)
                order by count(*) desc''')

    results2 = engine.execute(sql2).fetchall()
    return results2