
from dataclasses import dataclass
import pandas as pd 
import os
from src.logger import logging

from src.exception import CustomException
import sys
from sklearn.preprocessing import StandardScaler
from src.utils.utils import save_object
from typing import Union
from typing_extensions import Annotated
from keras.utils import to_categorical
from src.entity.entity_config import DataPreprocessingConfig



    

class DataPreprocessing:
    
    def __init__(self,config:DataPreprocessingConfig) -> None:
       
        self.config = config
    
    def initiate_data_preprocessing(self,train_path:str,test_path:str)->Union[
        Annotated[pd.DataFrame,"X_train"],
        Annotated[pd.Series,"y_train"],
        Annotated[pd.DataFrame,"X_test"],
        Annotated[pd.DataFrame,"y_test"]
    ]:
       try:
            logging.info("<++++++++++++ Data Preprocessing Started ++++++++++++++>")
            self.preprocessor = StandardScaler()
            train = pd.read_csv(train_path)
            test = pd.read_csv(test_path)
            
            X_train,y_train,X_test,y_test = (
                train.drop(columns=["label"]),train["label"],
                test.drop(columns=["label"]),test["label"]
            )
            
            X_train = self.preprocessor.fit_transform(X_train)
            X_test = self.preprocessor.transform(X_test)
            
            y_train = to_categorical(y_train)
            y_test = to_categorical(y_test)
            
            save_object(self.config.preprocessor_path,self.preprocessor)
            logging.info("<++++++++++++ Data Preprocessing Completed ++++++++++++++>")
            
            return X_train,y_train,X_test,y_test
       except Exception as e:
           raise CustomException(e,sys)

        
        