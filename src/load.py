# import libraries
import sqlite3
import logging 
from config import DB_PATH, TABLE_NAME

logger = logging.getLogger(__name__)

def loading(df, table_name):
    "load db into sqlite3 database"
    try: 
        logger.info(f"Loading {len(df)} rows into {DB_PATH}")
        conn = sqlite3.connect(DB_PATH)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        logger.info("Load complete")
    except Exception as e: 
        logger.error(f"Data hasnt be loading into databse {(e)}")
        return None
