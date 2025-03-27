from mongo_utils import fetch_data
import pandas as pd
import numpy as np
from scipy import stats

def process_weather(theday):
    df = fetch_data('weatherCom', theday)
    df = df[['uv', 'Humidity', 'pytime', 'hweather', 'temp', 'tempFeels', 'city']]
    df['uv'] = df['uv'].str.replace('紫外線指數', '').str.replace('(最大值 10)', '').astype(int)
    df['year'] = df['pytime'].str[0:4]
    df['mon'] = df['pytime'].str[5:7]
    df['day'] = df['pytime'].str[8:10]
    df['hour'] = df['pytime'].str[11:13]
    df = df.drop(columns=['pytime'])
    df['county'] = df['city'].apply(lambda x: x.split(',')[0])
    df['city'] = df['city'].apply(lambda x: x.split(',')[1])
    df['tempFeels'] = df['tempFeels'].str.replace('體感溫度 ', '').str.replace('°', '').astype(int)
    df['temp'] = df['temp'].str.replace('°', '').astype(int)
    df['Humidity'] = df['Humidity'].str.replace('%', '').astype(int)
    df['hourint'] = df['hour'].astype(int)
    df614 = df[(df['hourint'] > 5) & (df['hourint'] < 15)]
    df1523 = df[(df['hourint'] > 14) & (df['hourint'] < 24)]
    return clean(df614), clean(df1523)

def clean(df):
    df['city'] = df['city'].replace(' 臺灣省', '桃園市')
    avg = df.groupby('city').mean().astype(int).reset_index().sort_values('city')
    day = df.groupby('city').head(1)[['city', 'year', 'mon', 'day', 'hour', 'county']].sort_values('city')
    weather = df.groupby('city')['hweather'].apply(list).reset_index()
    weather['hweather'] = weather['hweather'].apply(lambda x: stats.mode(x)[0][0])
    return weather.merge(avg).merge(day).drop(columns='hourint', errors='ignore')
