# citibike_analysis

An examination ridership data for the NYC Citibike program in 2016 and 2017. 

I downloaded the individual month files from January 2016 to December 2017 from the citibike website and unzipped them all into a single folder. From there I used a python script to set up a for loop that would upload the data from each file in turn into a table in a MySQL database. Before uploading I stripped out the informaton for the individual bike stations, except for the station ID, to normalize the table and reduce its size by reducing redundant data. I uploaded a second table with the bike station information that could be joined if necesary.

One SQL query pulls together an aggregated list of trips by start and end station, as well as usertype, month, and year. I put this data into tableau public along with the information from the station table in the database and was able to create a map showing the Top 10 stations by number of trips.

The data used in the analysis in the powerpoint deck came from the attached Jupyter Notebooks mainly using the Pandas library to work with the data in dataframes and the matplotlib library to create charts. 

Files:

1 - citibike_data_examination_quries.sql - the queries used to examine the data and generate a dataset that was used in a tableau workbook. Written in MySQL

2 - upload_to_db.py - a python script used to upload the full dataset to a MySQL database

3 - bike_station_table_creation.py - a python script used to upload the information about the bike stations

4 - citibike_ridership_analysis.pptx - an analysis of the data with a view to finding potential incremental revenue

5 - citibike_data_analysis.ipynb - jupyter notebook with further analysis of the citibike data.

Please also take a look at this tableau workbook to see the top 10 most used stations in the Citibike network over the two year period examined. https://public.tableau.com/app/profile/matt.singleton/viz/citibike_ridership_analysis/Dashboard2
