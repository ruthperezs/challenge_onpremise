import requests
import json
from fastavro import writer, parse_schema,fastavro
from sqlalchemy.orm import Session
from datetime import date

today = date.today()
schema_separated_job = {
    'name': 'Job',
    'namespace': 'avro.job',
    'type': 'record',
    'fields': [
        {'name': 'id', 'type': 'int'},
        {'name': 'job', 'type': 'string'}
    ]
}

schema_separated_dep = {
    'name': 'Department',
    'namespace': 'avro.department',
    'type': 'record',
    'fields': [
        {'name': 'id', 'type': 'int'},
        {'name': 'department', 'type': 'string'}
    ]
}

schema_separated_hempl = {
    'name': 'Hired_employees',
    'namespace': 'avro.hempl',
    'type': 'record',
    'fields': [
        {'name': 'id', 'type': 'int'},
        {'name': 'name', 'type': 'string'},
        {'name': 'datetime', 'type': 'string'},
        {'name': 'department_id', 'type': 'int'},
        {'name': 'job_id', 'type': 'int'}
    ]
}


def do_backup1(db: Session):
    URL = 'http://localhost:8000/hiredemployees'

    response = requests.get(URL)

    data = response.json()

    parsed_schema = parse_schema(schema_separated_hempl)

    with open('bkp_avro/hired_employees.avro', 'wb') as f:
        fastavro.writer(f, parsed_schema, data)

    return "Backup realizado"

def do_backup2(db: Session):
    URL = 'http://localhost:8000/jobs'

    response = requests.get(URL)

    data2 = response.json()

    parsed_schema = parse_schema(schema_separated_dep)

    with open('bkp_avro/dept.avro', 'wb') as f:
        fastavro.writer(f, parsed_schema, data2)

    return "Backup realizado"

def do_backup3(db: Session):
    URL = 'http://localhost:8000/departments'

    response = requests.get(URL)

    data3 = response.json()

    parsed_schema = parse_schema(schema_separated_job)

    with open('bkp_avro/jobs.avro', 'wb') as f:
        fastavro.writer(f, parsed_schema, data3)

    return "Backup realizado"
