import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv.main import load_dotenv,find_dotenv
BASEDIR = os.path.abspath(os.path.dirname(__file__))

#print(load_dotenv('.env'))
#SQLALCHEMY_DATABASE_URL = os.getenv('CONN')

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:octubre@localhost:5432/db_challenge"
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bin=engine,autocommit=False,autoflush=False)
Base = declarative_base()
