import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from src.mlproject.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    logging.info("the execution started")
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("logging started")
        raise CustomException(e, sys)
