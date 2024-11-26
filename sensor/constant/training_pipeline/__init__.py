import os

TARGET_COLUMN = "class"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR = "artifact"
FILE_NAME = "sensor.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"

"""
Data Ingestion related constants 
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_NAME: str = "feature_store"
DATA_INGESTION_INGESTED_DIR_NAME: str = "ingested_data"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25


"""
Data Validation related constants
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR_NAME:str = "validated"
DATA_VALIDATION_INVALID_DIR_NAME:str = "Invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR_NAME:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"