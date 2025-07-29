import logging
import os 
from datetime import datetime

# Log fayl adı (vaxta əsaslanaraq)
Log_file = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'

# logs/ qovluğunun yaradılması
logs_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_dir, exist_ok=True)

# Log faylının tam yolu
Log_file_path = os.path.join(logs_dir, Log_file)

# Logging konfiqurasiyası
logging.basicConfig(
    filename=Log_file_path,
    format="%(asctime)s - %(levelname)s - %(name)s - %(lineno)d - %(message)s",
    level=logging.INFO
)

# Test log
if __name__ == '__main__':
    logging.info("Logging has started")
