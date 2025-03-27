from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd
import datetime
import os

def befortdate(num):
    date = datetime.date.today() + datetime.timedelta(days=num)
    return date.year, date.month, date.day

def object_id_from_datetime(dt=None):
    if not dt:
        dt = datetime.datetime.now()
    return ObjectId.from_datetime(generation_time=dt)

def mongodate(y, m, d):
    dt = datetime.datetime(y, m, d) + datetime.timedelta(hours=-8)
    return object_id_from_datetime(dt)

def fetch_data(collection, theday):
    mongoip = os.getenv('MONGO_HOST')
    start_y, start_m, start_d = befortdate(theday+1)
    end_y, end_m, end_d = befortdate(theday)
    start_ts = mongodate(start_y, start_m, start_d)
    end_ts = mongodate(end_y, end_m, end_d)
    client = MongoClient(f'mongodb://{mongoip}:27017/')
    db = client['weather']
    col = db[collection]
    query = {"_id": {"$gte": end_ts, "$lt": ObjectId(start_ts)}}
    return pd.DataFrame(list(col.find(query)))
