

from src.utils.utils import read_yaml
from src.entity.entity_config import DataIngestionConfig,DataPreprocessingConfig,TrainModelConfig,EvaluateModelConfig
class ConfigManeger:
    
    def __init__(self,
                 config_path=CONFIG_PATH,
                 params_path=PARAMS_PATH
                 ) -> None:
        self.config = read_yaml(config_path)
    
    def get_ingest_data_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        data_ingestion_config = DataIngestionConfig(data_url=config.data_url,
            data_extract_path=config.extract_data_path,
            download_data_path=config.download_path,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            raw_data_path=config.raw_data_path)

        return data_ingestion_config
    
    def get_data_preprocessing_config(self)->DataPreprocessingConfig:
        config = self.config.data_preprocessing
        data_preprocessing_config = config.data_preprocessor_path
        return data_preprocessing_config
        
    def get_train_model_config(self)->TrainModelConfig:
        config = self.config.train_model
        train_model_config= TrainModelConfig(trained_model_path=config.trained_model_path)
        return train_model_config    

    def get_evaluate_model_config(self)->EvaluateModelConfig:
        config:self.evaluate_model
        evaluate_model_config = EvaluateModelConfig(trained_model_path=config.trained_model_path)
        return evaluate_model_config