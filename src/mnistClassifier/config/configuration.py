

from mnistClassifier.utils.utils import read_yaml
from mnistClassifier.entity.entity_config import DataIngestionConfig,DataPreprocessingConfig,TrainModelConfig,EvaluateModelConfig,BuildModelConfig
from mnistClassifier.constant import *
class ConfigManeger:
    
    def __init__(self,
                 config_path=CONFIG_FILE_PATH,
                 params_path=PARAMS_FILE_PATH
                 ) -> None:
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
    
    def get_ingest_data_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        data_ingestion_config = DataIngestionConfig(data_url=config.data_url,
            data_extract_path=config.extract_data_path,
            download_data_path=config.download_path,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            raw_data_path=config.raw_data_path)

        return data_ingestion_config
    
    def get_build_model_config(self)->BuildModelConfig:
        config = self.config.build_config
        buidl_model_config = BuildModelConfig(build_model_path=config.model_build_path,dense_size=self.params.DENSE_SIZE)
        return buidl_model_config
    
    def get_data_preprocessing_config(self)->DataPreprocessingConfig:
        config = self.config.data_preprocessing
        data_preprocessing_config = DataPreprocessingConfig(
            preprocessor_path=config.data_preprocessor_path,
            train_path=config.train_path,
            test_path=config.test_path
        )
        
        return data_preprocessing_config
        
    def get_train_model_config(self)->TrainModelConfig:
        config = self.config.train_model
        params = self.params
        train_model_config= TrainModelConfig(trained_model_path=config.trained_model_path,
             epochs=params.EPOCHS,
             batch_size=params.BATCH_SIZE)
        return train_model_config    

    def get_evaluate_model_config(self)->EvaluateModelConfig:
        config = self.config.evaluate_model
        evaluate_model_config = EvaluateModelConfig(trained_model_path=config.trained_model_path,
                                                    all_params=self.params)
        return evaluate_model_config