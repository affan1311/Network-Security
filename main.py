from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.my_logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        dataingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info('Data ingestion config done')
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
   