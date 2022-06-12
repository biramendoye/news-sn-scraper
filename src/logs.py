import logging
import os


PROJECT_NAME = "news-sn-scraper"
BASE_DIR = os.getcwd()
LOG_FILE = os.path.join(BASE_DIR, f'{PROJECT_NAME}.log')

logger = logging.getLogger(PROJECT_NAME)
f_handler = logging.FileHandler(LOG_FILE)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
f_handler.setLevel(logging.DEBUG)
logger.addHandler(f_handler)

def log_info(_message):
    logger.info(_message)

def log_warning(_message):
    logger.warning(_message)

def log_error(_message):
    logger.error(_message)
