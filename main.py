import sys
from sensor.logger import logging
from sensor.expection import SensorException
from sensor.pipeline import training_pipeline

if __name__=="__main__":
    logging.info("---- WELCOME TO Air Pressure system (APS) Project ----")
    
    try:
       data_trainer = training_pipeline.TrainPipeline()
       data_trainer.run_pipeline()   

       
        
    except Exception as e:
        logging.error(SensorException(e, sys)) 