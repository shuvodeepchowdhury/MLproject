import logging
import os
from datetime import datetime

# Define the log directory and file name
LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_PATH = os.path.join(os.getcwd(), LOG_DIR)

# Ensure the log directory exists
os.makedirs(LOG_PATH, exist_ok=True)

# Construct the full log file path
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
