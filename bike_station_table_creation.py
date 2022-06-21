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

bike_stations = pd.DataFrame()
print(type(bike_stations))

for file in files_to_use:
    citibike_data = pd.read_csv(file)
    citibike_data.columns = data_columns
    start_stations = citibike_data[['start_station_id', 'start_station_name', 'start_station_latitude', 'start_station_longitude']]
    start_stations.columns = ['station_id','station_name','station_latitude','station_longitude']
    start_stations = start_stations.drop_duplicates(subset='station_id')
    record_count = record_count+len(start_stations)
    bike_stations = bike_stations.append(start_stations)
    bike_stations = bike_stations.drop_duplicates(subset='station_id')
    print(file,' ',len(start_stations),' ',record_count,' ',len(bike_stations))

for file in files_to_use:
    citibike_data = pd.read_csv(file)
    citibike_data.columns = data_columns
    end_stations = citibike_data[['end_station_id', 'end_station_name', 'end_station_latitude', 'end_station_longitude']]
    end_stations.columns = ['station_id','station_name','station_latitude','station_longitude']
    end_stations = end_stations.drop_duplicates(subset='station_id')
    record_count = record_count+len(end_stations)
    bike_stations = bike_stations.append(end_stations)
    bike_stations = bike_stations.drop_duplicates(subset='station_id')
    print(file,' ',len(end_stations),' ',record_count,' ',len(bike_stations))

engine = create_engine("mysql://{user}:{pw}@localhost/{db}"  
                    .format(user="root", pw=BBBBBBB, 
                    db="koho_assignment"))

bike_stations.to_sql('citibike_stations', con=engine,if_exists='append',chunksize=1000,index=False)