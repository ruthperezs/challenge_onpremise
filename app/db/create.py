import psycopg2

try:
    conn = psycopg2.connect(database = "db_challenge", user = "postgres", password = "octubre", host = "localhost", port = "5432")
except:
    print("No se pudo establecer conexion") 

cur = conn.cursor()
conn.autocommit = True
try:
    create1='''CREATE TABLE IF NOT EXISTS hired_employees (ID INT NOT NULL, 
            NAME VARCHAR(100),DATETIME VARCHAR(20), 
            DEPARTAMENT_ID INT,JOB_ID INT,PRIMARY KEY (ID));'''
    cur.execute(create1)
except:
    print("Error:No se creó tabla hired_employees")

try:
    create2='''CREATE TABLE IF NOT EXISTS jobs (ID INT NOT NULL,JOB VARCHAR(200),PRIMARY KEY (ID));'''
    cur.execute(create2)
except:
    print("Error:No se creó tabla jobs")

try:
    create3='''CREATE TABLE IF NOT EXISTS departments (ID INT NOT NULL,DEPARTAMENT VARCHAR(30),PRIMARY KEY (ID));'''
    cur.execute(create3)
except:
    print("Error:No se creó tabla departments")

###carga de datos en las tablas
try:
    c1='''COPY hired_employees(id,name,datetime,department_id,job_id) FROM 'C:\GIT_ACT\challenge_onpremise\doc\hired_employees.csv' DELIMITER ',' CSV;'''
    cur.execute(c1)
except:
    print("Error: no se realizó la carga hired_employees")

try:
    c2='''COPY departments(id,department) FROM 'C:\GIT_ACT\challenge_onpremise\doc\departments.csv' DELIMITER ',' CSV;'''
    cur.execute(c2)
except:
    print("Error: no se realizó la carga departments")

try:
    c3='''COPY jobs(id,job) FROM 'C:\GIT_ACT\challenge_onpremise\doc\jobs.csv' DELIMITER ',' CSV;'''
    cur.execute(c3)
except:
    print("Error: no se realizó la carga jobs")

 # <--- makes sure the change is shown in the database
conn.close()
cur.close()