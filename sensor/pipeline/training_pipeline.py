from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.components.data_ingestion import DataIngestion

from sensor.expection import SensorException
import sys,os
from sensor.logger import logging



from sensor.entity.artifact_entity import DataValidationArtifact
from sensor.entity.config_entity import DataValidationConfig
from sensor.components.data_validation import DataValidation





class TrainPipeline:
    is_pipeline_running = False

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()


    def start_data_ingestion(self)->DataIngestionArtifact:

        try:
            
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)

            logging.info("Starting data ingestion")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact
        
        except  Exception as e:
            raise  SensorException(e,sys)
        
    
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data Validation")
            
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_config=data_validation_config)

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info(f"Data Validation completed and artifact: {data_validation_artifact}")
            
            return data_validation_artifact

        except  Exception as e:
            raise  SensorException(e,sys)
        
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)

        except Exception as e:
            raise SensorException(e, sys)