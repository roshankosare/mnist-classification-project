
from dataclasses import dataclass
import pandas as pd 
import os
from src.logger import logging
from sklearn.model_selection import train_test_split
from src.exception import CustomException
import sys
from src.utils.utils import download_file,extract_zip
from src.entity.entity_config import DataIngestionConfig


class IngestData:
    
    def __init__(self,config:DataIngestionConfig) -> None:
       
        self.config = config
        os.makedirs(os.path.dirname(self.config.test_data_path),exist_ok=True)
        
    def download_data(self):
        try:
            download_file(self.url,self.config.download_data_path)
        except Exception as e:
            raise CustomException(e,sys)
    
    def extract_zip(self):
        extract_zip(self.config.download_data_path,self.config.data_extract_path)
    
    def intiate_data_ingestion(self)->DataIngestionConfig:
        logging.info("<+++++++++++ Started Data Ingestion +++++++++++>")
        try:
            logging.info("<+++++++++++++Downloding Data Started ++++++++++++>")
            self.download_data()
            logging.info("<+++++++++++++Downloding Data Completed++++++++++++>")
            logging.info("<+++++++++++++Extracting  Data Started ++++++++++++>")
            self.extract_zip()
            logging.info("<+++++++++++++EXtracting  Data Completed ++++++++++++>")
            df = pd.read_csv(self.config.raw_data_path)
            train,test= train_test_split(df,test_size=0.2,random_state=42)
            train.to_csv(self.config.train_data_path,index = False,header = True)
            test.to_csv(self.config.test_data_path,index = False,header = True)
            logging.info("<+++++++++++ Data Ingestion Completed +++++++++++>")
        except Exception as e:
            raise CustomException(e,sys)