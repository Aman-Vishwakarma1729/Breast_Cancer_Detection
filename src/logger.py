import os 
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
   
        file_name = LOG_FILE_PATH,
        format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level = logging.INFO 

)
        