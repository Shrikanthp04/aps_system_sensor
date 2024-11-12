import sys
from sensor.logger import logging
from sensor.expection import SensorException

if __name__=="__main__":
    logging.info("---- WELCOME TO Air Pressure system (APS) Project ----")
    
    try:
        ls = [1,2]
        ls[4]
        
    except Exception as e:
        logging.error(SensorException(e, sys)) 