# import libraries
import pandas as pd
import logging
from config import DATA_URL, NOC_URL

# set up logging
logger = logging.getLogger(__name__)

def data_extract(data_url): 
    "load data_url and return df"
    try: 
        logger.info(f"Extracting data from {data_url}")
        data = pd.read_csv(data_url)
        logger.info(f"Dataframe has {len(data)} rows")
        #print(data)
        return data
    except Exception as e:
        logger.error(f"Faild to extract data {e}")
        return None