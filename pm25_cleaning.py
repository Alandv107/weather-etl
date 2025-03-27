from mongo_utils import fetch_data
import pandas as pd
import numpy as np
from scipy import stats

def process_pm25(theday):
    df = fetch_data('pm25json', theday)
    df = df[['PublishTime', 'PM25_AVG', 'County', 'Status']]
    df['year'] = df['PublishTime'].str[0:4]
    df['mon'] = df['PublishTime'].str[5:7]
    df['day'] = df['PublishTime'].str[8:10]
    df['hour'] = df['PublishTime'].str[11:13]
    df['PM25_AVG'] = df['PM25_AVG'].replace('', np.nan).astype(float)
    df['city'] = df['County']
    df = df.drop(columns=['PublishTime', 'County'])
    df['hourint'] = df['hour'].astype(int)
    df614 = df[(df['hourint'] > 5) & (df['hourint'] < 15)]
    df1523 = df[(df['hourint'] > 14) & (df['hourint'] < 24)]
    return clean(df614), clean(df1523)

def clean(df):
    avg = df.groupby('city').mean().astype(int).reset_index().sort_values('city')
    day = df.groupby('city').head(1)[['city', 'year', 'mon', 'day', 'hour']].sort_values('city')
    status = df.groupby('city')['Status'].apply(list).reset_index()
    status['Status'] = status['Status'].apply(lambda x: stats.mode(x)[0][0])
    return status.merge(avg).merge(day).drop(columns='hourint', errors='ignore')
