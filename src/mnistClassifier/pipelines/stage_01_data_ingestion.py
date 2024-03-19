

import sys
from mnistClassifier.exception import CustomException
from mnistClassifier.components.ingest_data import IngestData
from mnistClassifier.logger import logging
from mnistClassifier.config.configuration import ConfigManeger


class DataIngestionStage:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigManeger()
        data_ingestion_config = config.get_ingest_data_config()
        data_ingest = IngestData(config=data_ingestion_config)
        data_ingest.intiate_data_ingestion()


if __name__ == "__main__":
    try:
        data_ingestion = DataIngestionStage()
        data_ingestion.main()
    except Exception as e:
        raise CustomException(e,sys)
    