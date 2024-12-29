
import pandas as pd

def transform(df):
    max_latitude = df['latitude'].max()
    return df[df['latitude'] == max_latitude]
