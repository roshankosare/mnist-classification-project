import sys
from src.exception import CustomException
from src.config.configuration import ConfigManeger
from src.components.data_preprocessing import DataPreprocessing
from src.components.train_model import TrainModel


class TrainModelStep:
    def __init__(self) -> None:
        pass
    
    def main():
        config = ConfigManeger()
        data_preprocessing_config = config.get_data_preprocessing_config()
        train_model_config = config.get_train_model_config()
        
        data_preprocessor = DataPreprocessing(config=data_preprocessing_config)
        model_trainer = TrainModel(config=train_model_config)
        
        X_train,y_train,X_test,y_test = data_preprocessor.initiate_data_preprocessing()
        model_trainer.initiate_model_training(X_train,y_train,X_test,y_test)
        
    
if __name__ == "__main__":
    try:
        model_train_stage = TrainModelStep()
        model_train_stage.main()
    except Exception as e:
        raise CustomException(e,sys)