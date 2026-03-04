import pandas
import sys
sys.path.append('src')
from transform import transform

# tests/test_transform.py
import sys
sys.path.append('src')

import pandas as pd
from transform import transform

def make_test_df():
    "reusable test dataframe"
    return pd.DataFrame({
        'Season': ['Winter', 'Summer', 'Winter'],
        'Sex': ['M', 'F', 'M'],
        'Age': [25.0, 30.0, None],
        'Height': [180.0, 165.0, None],
        'Weight': [75.0, 60.0, None],
        'Medal': ['Gold', None, 'Bronze']
    })

def test_transform_filters_winter():
    "only winter rows should remain"
    result = transform(make_test_df())
    assert all(result['Season'] == 'Winter')

def test_transform_no_null_age():
    "no null values in Age after transform"
    result = transform(make_test_df())
    assert result['Age'].isnull().sum() == 0

def test_transform_medal_none():
    "NaN medals should be replaced with None"
    result = transform(make_test_df())
    assert result['Medal'].isnull().sum() == 0