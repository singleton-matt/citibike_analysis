-- A query to get a high level overview of the data set
SELECT 
    YEAR(date_start) AS year_rent_bike,
    COUNT(*) AS num_trips,
    ROUND(AVG((tripduration / 60)), 2) AS avg_trip_duration_minutes
FROM
    koho_assignment.full_data
GROUP BY year_rent_bike

-- Examine the behaviours of subscribers and non-subscribers by year
SELECT 
    YEAR(date_start) AS year_rent_bike,
    usertype,
    COUNT(*) AS num_trips,
    COUNT(*) / (SELECT 
            COUNT(*)
        FROM
            koho_assignment.full_data
        WHERE
            YEAR(date_start) = 2016) AS percent_of_total_trips,
    ROUND(AVG((tripduration / 60)), 2) AS avg_trip_duration_minutes
FROM
    koho_assignment.full_data
WHERE
    YEAR(date_start) = 2016
GROUP BY year_rent_bike , usertype 
UNION SELECT 
    YEAR(date_start) AS year_rent_bike,
    usertype,
    COUNT(*) AS num_trips,
    COUNT(*) / (SELECT 
            COUNT(*)
        FROM
            koho_assignment.full_data
        WHERE
            YEAR(date_start) = 2017) AS percent_of_total_trips,
    ROUND(AVG((tripduration / 60)), 2) AS avg_trip_duration_minutes
FROM
    koho_assignment.full_data
WHERE
    YEAR(date_start) = 2017
GROUP BY year_rent_bike , usertype

-- Examine the birth year of users. There were some issues with data - extremely low birth years, so this field is not going to be used in this analysis
SELECT 
    YEAR(date_start) AS year_rent_bike,
    usertype,
    min(birthyear),max(birthyear)
FROM
    koho_assignment.full_data
GROUP BY year_rent_bike , usertype

-- Generate a csv that can be uploaded to tableau to analyze station usage patterns
SELECT 
    usertype,
    YEAR(date_start) AS year,
    MONTH(date_start) AS month,
    start_station_id AS station_id,
    COUNT(tripduration) AS number_of_trips,
    SUM(tripduration) AS total_trip_time,
    'trip_start' AS trip_type
FROM
    koho_assignment.full_data
WHERE
    usertype = 'Subscriber'
GROUP BY usertype , YEAR(date_start) , MONTH(date_start) , start_station_id 
UNION SELECT 
    usertype,
    YEAR(date_start) AS year,
    MONTH(date_start) AS month,
    end_station_id AS station_id,
    COUNT(tripduration) AS number_of_trips,
    SUM(tripduration) AS total_trip_time,
    'trip_end' AS trip_type
FROM
    koho_assignment.full_data
GROUP BY usertype , YEAR(date_start) , MONTH(date_start) , end_station_id
