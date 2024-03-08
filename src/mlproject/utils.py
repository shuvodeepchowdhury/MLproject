import os
import pandas as pd
import pymysql
from dotenv import load_dotenv  # Import load_dotenv function
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from dataclasses import dataclass  # Import dataclass module

load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
passwd = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("reading my sql started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=passwd,
            db=db
        )
        logging.info("connection established with the db")
        df = pd.read_sql_query("select * from students", mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex)
