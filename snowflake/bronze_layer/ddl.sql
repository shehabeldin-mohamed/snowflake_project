USE DATABASE AIRLINE_EDW;
USE SCHEMA AIRLINE_EDW.BRONZE;

CREATE OR REPLACE TABLE RAW(
    passenger_id VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    age INT,
    nationality VARCHAR,
    airport_name VARCHAR,
    airport_country_code VARCHAR,
    country_name VARCHAR,
    airport_continent STRING,
    continents VARCHAR,
    departure_date DATE,
    arrival_airport VARCHAR,
    pilot_name VARCHAR,
    flight_status VARCHAR,
    ticket_type VARCHAR,
    passenger_status VARCHAR
);
