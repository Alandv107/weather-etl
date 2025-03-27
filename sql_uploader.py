import os
from sqlalchemy import create_engine

def upload_to_sql(df):
    user = os.getenv('SQL_USER')
    passwd = os.getenv('SQL_PASS')
    host = os.getenv('SQL_HOST')
    db = os.getenv('SQL_DB')
    engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}/{db}?charset=utf8")
    with engine.connect() as con:
        df.to_sql(name='weather', con=con, if_exists='append', index=False)
