
import sys
from mnistClassifier.config.configuration import ConfigManeger
from mnistClassifier.components.evaluate_model import EvaluateModel
from mnistClassifier.exception import CustomException
from mnistClassifier.components.data_preprocessing import DataPreprocessing


class EvaluateModelStage:
  
    def __init__(self) -> None:
        pass
    
    def main(self):
            config  = ConfigManeger()
            model_evaluation_config = config.get_evaluate_model_config()
            data_preprocessing_config = config.get_data_preprocessing_config()
            data_preprocessor = DataPreprocessing(config=data_preprocessing_config)
            _,_,X_test,y_test = data_preprocessor.initiate_data_preprocessing()
            model_evaluator = EvaluateModel(config=model_evaluation_config)
            model_evaluator.initiate_model_evaluation(X_test,y_test)
    
        
        
if __name__ == "__main__":
    try:
        model_evaluator = EvaluateModelStage()
        model_evaluator.main()
    except Exception as e:
        raise CustomException(e,sys)