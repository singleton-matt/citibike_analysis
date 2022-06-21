from sqlalchemy import create_engine
import pandas as pd

data_columns = ['tripduration', 'starttime', 'stoptime', 'start_station_id', 'start_station_name', 'start_station_latitude', 'start_station_longitude', 'end_station_id', 'end_station_name', 'end_station_latitude', 'end_station_longitude', 'bikeid', 'usertype', 'birthyear', 'gender']
files_to_use = ["201606-citibike-tripdata.csv",
"201607-citibike-tripdata.csv",
"201608-citibike-tripdata.csv",
"201609-citibike-tripdata.csv",
"201610-citibike-tripdata.csv",
"201611-citibike-tripdata.csv",
"201612-citibike-tripdata.csv",
"201701-citibike-tripdata.csv",
"201702-citibike-tripdata.csv",
"201703-citibike-tripdata.csv",
"201704-citibike-tripdata.csv",
"201705-citibike-tripdata.csv",
"201706-citibike-tripdata.csv",
"201707-citibike-tripdata.csv",
"201708-citibike-tripdata.csv",
"201709-citibike-tripdata.csv",
"201710-citibike-tripdata.csv",
"201711-citibike-tripdata.csv",
"201712-citibike-tripdata.csv",
"201601-citibike-tripdata.csv",
"201602-citibike-tripdata.csv",
"201603-citibike-tripdata.csv",
"201604-citibike-tripdata.csv",
"201605-citibike-tripdata.csv"]

record_count = 0

for file in files_to_use:
    citibike_data = pd.read_csv(file)
    citibike_data.columns = data_columns
    citibike_data.drop(['start_station_name', 'start_station_latitude', 'start_station_longitude', 'end_station_name', 'end_station_latitude', 'end_station_longitude'],axis=1,inplace=True)
    record_count = record_count+len(citibike_data)
    print(file,' ',len(citibike_data),' ',record_count)
    engine = create_engine("mysql://{user}:{pw}@localhost/{db}"  
                        .format(user="root", pw=bbbbbbb, 
                        db="koho_assignment"))

    citibike_data.to_sql('citibike_tripdata_full', con=engine,if_exists='append',chunksize=1000,index=False)