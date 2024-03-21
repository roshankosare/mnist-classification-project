

import sys
from mnistClassifier.components.build_model import BuildModel
from mnistClassifier.config.configuration import ConfigManeger
from mnistClassifier.exception import CustomException

class BuildModelStage:
    def __init__(self) -> None:
        pass
    
    def main(self):
       try:
            config = ConfigManeger()
            model_build_config = config.get_build_model_config()
            model_builder = BuildModel(config=model_build_config)
            model_builder.build_model()
       except Exception as e:
           raise CustomException(e,sys)
    

if __name__ == "__main__":
    build_stage = BuildModelStage()
    build_stage.main()