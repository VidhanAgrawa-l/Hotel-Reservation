import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True) # make a directory of name LOGS_DIR whcih is logs, if it does not exist

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")# create a log file inside the logs directory with the name log_YYYY-MM-DD.log

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)# configure the logging module to write logs to the log file, with the format as specified above and the level as INFO
# the level INFO means that only logs with level INFO or higher will be written to the log file,higher levels are DEBUG,WARNING,ERROR,CRITICAL

def get_logger(name):# to initialize a logger with the name as specified in the argument
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger