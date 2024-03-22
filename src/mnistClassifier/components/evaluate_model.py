from dataclasses import dataclass
import pandas as pd 
import os
from mnistClassifier.logger import logging
import numpy as np
import mlflow
import keras
from mnistClassifier.exception import CustomException
import sys
from mnistClassifier.utils.utils import load_object
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import load_model
from mnistClassifier.entity.entity_config import EvaluateModelConfig

class EvaluateModel:
    def __init__(self,config:EvaluateModelConfig) -> None:
        self.config = config
        self.model:keras.Model
        
    def initiate_model_evaluation(self,X_test:pd.DataFrame,y_test:pd.DataFrame):
        
        try:
            logging.info("<++++++++++++++ Model Evaluation Started ++++++++++++>")
            self.model = load_model(self.config.trained_model_path)
            X_test = np.array(X_test).reshape(X_test.shape[0], 28, 28, 1)
            self.score = self.model.evaluate(X_test,y_test)
            logging.info("Accracy Score:{}".format(self.score[1]))
            logging.info("<++++++++++++++ Model Evaluation Started ++++++++++++>")
        except Exception as e:
            raise CustomException(e,sys)
    
    
    def mlflow_log_model(self):
    
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({
                "loss":self.score[0],
                "accuracy_socre":self.score[1]
            })
            
            mlflow.keras.log_model(self.model,"model")