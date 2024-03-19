
import sys
from src.config.configuration import ConfigManeger
from src.components.evaluate_model import EvaluateModel
from src.exception import CustomException


class EvaluateModelStage:
    
    def __init__(self) -> None:
        pass
    
    def main():
        config= ConfigManeger()
        model_evaluation_config = config.get_evaluate_model_config
        model_evaluator = EvaluateModel(config=model_evaluation_config)
        model_evaluator.initiate_model_evaluation()
        
        
if __name__ == "__main__":
    try:
        model_evaluator = EvaluateModelStage()
        model_evaluator.main()
    except Exception as e:
        raise CustomException(e,sys)