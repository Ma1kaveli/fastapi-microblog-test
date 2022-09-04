# import databases

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config


DB_CONNECTION = config("db_connection")
DB_HOST = config("db_host")
DB_PORT = config("db_port")
DB_DATABASE = config("db_database")
DB_USERNAME = config("db_username")
DB_PASSWORD = config("db_password")

SQLALCHEMY_DATABASE_URL = f"{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

        