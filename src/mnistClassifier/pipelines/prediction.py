import os
from tensorflow.keras.models import load_model
import pandas as pd
from src.utils.utils import load_object



class PredictionPipeline:
    
    def __init__(self) -> None:
         self.model_path = os.path.join("artifacts","model","model.h5")
         self.model = None
         self.preprocessor_path = os.path.join("artifacts","model","preprocessor.pkl")
         self.preprocessor = None
    
    def load_model(self):
        self.model = load_model(self.model_path)
        self.preprocessor = load_object(self.preprocessor_path)
        
    
    def make_prediction(self,x_data:pd.DataFrame):
        result  = self.model.predict(x_data);
        return result
    
    def preprocesses_data(self,X_data:pd.DataFrame):
        data = self.preprocessor.transform(X_data)
        return data