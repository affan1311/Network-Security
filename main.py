from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.my_logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        dataingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info('Data ingestion config done')
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info('Data ingestion done')
        print(dataingestionartifact)

        datavalidationconfig = DataValidationConfig(training_pipeline_config=trainingpipelineconfig)
        datavalidation = DataValidation(data_ingestion_artifact=dataingestionartifact, data_validation_config=datavalidationconfig)
        logging.info('Data validation config done')
        datavalidationartifact = datavalidation.initiate_data_validation()
        logging.info('Data validation done')
        print(datavalidationartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
   