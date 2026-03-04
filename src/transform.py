import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform(df): 
    "improve data quality"
    try: 
        logger.info(f"Transforming {len(df)} rows") 
        df = df[df['Season']== "Winter"]
        df['Age'] = df.groupby('Sex')['Age'].transform(lambda x: x.fillna(x.mean()))
        df['Age'] = df['Age'].astype(int)
        df['Height'] = df.groupby('Sex')['Height'].transform(lambda x: x.fillna(x.mean()))
        df['Height'] = df['Height'].astype(int)
        df['Weight'] = df.groupby('Sex')['Weight'].transform(lambda x: x.fillna(x.mean()))
        df['Weight'] = df['Weight'].astype(int)
        df['Medal'] = df['Medal'].fillna("None")
        logger.info(f"Transform complete: {len(df)} rows")
        return df
    except Exception as e: 
        logger.error(f"An exception was raised during transforming data {e}")
        return None