from dataclasses import dataclass
import pandas as pd 
import os
from src.logger import logging
import numpy as np


from src.exception import CustomException
import sys
from src.utils.utils import load_object
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import load_model
from src.entity.entity_config import EvaluateModelConfig

class EvaluateModel:
    def __init__(self,config:EvaluateModelConfig) -> None:
        self.config = config
        
    def initiate_model_evaluation(self,X_test:pd.DataFrame,y_test:pd.DataFrame):
        
        try:
            logging.info("<++++++++++++++ Model Evaluation Started ++++++++++++>")
            model = load_model(self.config.trained_model_path)
            X_test = np.array(X_test).reshape(X_test.shape[0], 28, 28, 1)
            result =  model.predict(X_test)

            y_test = np.argmax(y_test, axis=1)
            y_pred =  np.argmax(result, axis=1)

            self.accuracy_score = accuracy_score(y_test,y_pred)
            logging.info("Accracy Score:{}".format(self.accuracy_score))
            logging.info("<++++++++++++++ Model Evaluation Started ++++++++++++>")
        except Exception as e:
            raise CustomException(e,sys)