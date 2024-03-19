from dataclasses import dataclass
import pandas as pd 
import os
from src.logger import logging

from src.exception import CustomException
import sys

from src.components.models.cnn_mnist import CnnModel
import keras
from src.entity.entity_config import TrainModelConfig
   
    
class TrainModel:
    def __init__(self,config:TrainModelConfig) -> None:
       self.config = config
        
    def initiate_model_training(self,X_train:pd.DataFrame,y_train:pd.DataFrame,X_test:pd.DataFrame,y_test:pd.DataFrame)->ModelTrainConfig:
        
        try:
            logging.info("<++++++++++++ Model Training has Started ++++++++++++>")
            self.model = CnnModel()
            self.model.create_model()
            
            trained_model:keras.Model = self.model.train_model(X_train,y_train,X_test,y_test)
            logging.info("<++++++++++++ Model Training Completed")
            # trained_model.save(self.model_train_config.model_path)
            trained_model.save(self.config.trained_model_path)
        
        except Exception as e:
            raise CustomException(e,sys)