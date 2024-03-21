
import pandas as pd 
import os
from mnistClassifier.logger import logging

from mnistClassifier.exception import CustomException
import sys

from mnistClassifier.components.models.cnn_mnist import CnnModel
import keras
from mnistClassifier.entity.entity_config import TrainModelConfig
import numpy as np
   
    
class TrainModel:
    def __init__(self,config:TrainModelConfig) -> None:
       self.config = config
        
    def initiate_model_training(self,X_train:pd.DataFrame,y_train:pd.DataFrame,X_test:pd.DataFrame,y_test:pd.DataFrame):
        
        try:
            logging.info("<++++++++++++ Model Training has Started ++++++++++++>")
            model:keras.Model = keras.models.load_model(self.config.trained_model_path)
            
            # reshaping data as input shape required for model
            X_train = np.array(X_train).reshape(X_train.shape[0], 28, 28, 1)
            X_test =  np.array(X_test).reshape(X_test.shape[0], 28, 28, 1)
            
            # need to create new instance of optimizer for model and recompile model
            new_optimizer = keras.optimizers.Adam()
            model.compile(optimizer=new_optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
            
            model.fit(X_train,y_train,
             batch_size=self.config.batch_size,epochs=self.config.epochs)
            logging.info("<++++++++++++ Model Training Completed +++++++++++++++++++>")
           
            
            model.save(self.config.model_path)
        except Exception as e:
            raise CustomException(e,sys)