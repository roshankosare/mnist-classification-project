
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    data_url:str
    download_data_path:str
    train_data_path:str
    test_data_path:str
    data_extract_path:str
    raw_data_path:str


@dataclass(frozen=True)
class DataPreprocessingConfig:
    preprocessor_path:str
    train_path:str
    test_path:str
    
@dataclass(frozen=True)
class TrainModelConfig:
    trained_model_path:str
    
@dataclass(frozen=True)
class EvaluateModelConfig:
    trained_model_path:str
    
    