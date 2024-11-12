import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(LOG_FILE_PATH, exist_ok=True)
LOG_FILE_NAME = os.path.join(LOG_FILE_PATH, LOG_FILE)


logging.basicConfig(
    filename = LOG_FILE_NAME,
    format = "[%(asctime)s] %(levelname)s %(filename)s %(funcName)s %(lineno)d - %(message)s",
    level = logging.INFO,
)