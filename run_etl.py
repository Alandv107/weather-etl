from weather_cleaning import process_weather
from pm25_cleaning import process_pm25
from sql_uploader import upload_to_sql
import datetime

def main(theday):
    weather_df_mor, weather_df_night = process_weather(theday)
    pm_df_mor, pm_df_night = process_pm25(theday)
    pm_df_mor = pm_df_mor[pm_df_mor['Status'] != '設備維護']
    morning = weather_df_mor.merge(pm_df_mor[['city', 'Status', 'PM25_AVG']])
    night = weather_df_night.merge(pm_df_night[['city', 'Status', 'PM25_AVG']])
    morning['mornight'] = 'mor'
    night['mornight'] = 'night'
    final_df = morning.append(night)
    date = datetime.date.today() + datetime.timedelta(days=theday)
    final_df['week'] = date.strftime('%W')
    upload_to_sql(final_df)

if __name__ == '__main__':
    for i in range(-1, 0):
        main(i)
