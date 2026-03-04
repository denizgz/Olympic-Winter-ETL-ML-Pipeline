import sys
sys.path.append('src')

import logging
from extract import data_extract
from transform import transform
from load import loading
from config import DATA_URL, NOC_URL

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format= ("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

data_athletes = data_extract(DATA_URL)
data_noc = data_extract(NOC_URL)

if data_athletes is None: 
    logger.error("Extraction failed, stopping pipeline")
    exit(1)

if data_noc is None: 
    logger.error("Extraction failed, stopping pipeline")
    exit(1)

transform_athlethes = transform(data_athletes)
load_athletes = loading(transform_athlethes, "athletes")
load_noc = loading(data_noc, "noc")

