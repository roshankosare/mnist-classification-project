
import sys
from mnistClassifier.components.models.cnn_mnist import CnnModel
from mnistClassifier.entity.entity_config import BuildModelConfig
from mnistClassifier.exception import CustomException



class BuildModel:
    
    def __init__(self,config:BuildModelConfig) -> None:
        self.config = config
        
    def  build_model(self):
        
       try:
            model_builder = CnnModel(self.config.dense_size)
            model = model_builder.create_model()
            model.save(self.config.build_model_path)
       except Exception as e:
           raise CustomException(e,sys)
        
        
        