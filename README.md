# snowflake_project
This project showcases medallion architecture. The project is done using local airflow setup with snowflake. The pipeline starts by  a csv file into the bronze layer, cleans it and then loads it to the silver layer, and finally to the gold where it is ready for reporting. You can find the ddl scripts, time travel, and procedures used in snowflake for this project in the snowflake folder.

## Prerequisites
.env file containing the following: 
* AIRFLOW_UID=50000 
* _PIP_ADDITIONAL_REQUIREMENTS=apache-airflow-providers-snowflake

## Airline Dashboard
![Dashboard](assets/dashboard.png)

## Airflow Dag
![Airflow DAG showcasing the whole pipeline](assets/dag.png)

## Snowflake
### Bronze Layer
This layer is a 1-to-1 copy of the dataset
![sronze layer](assets/bronze_raw.png)

### Silver Layer
This layer is a cleaned copy of the dataset
![silver_layer](assets/silver_clean.png)

### Gold Layer
This layer introduces the star schema for easier reporting.
#### Fact_Flights Table
![fact_flights](assets/fact_flights.png)

#### Dim_Passenger Table
![passenger_dim](assets/dim_passenger.png)

#### Dim_Airport Table
![airport_dim](assets/dim_airport.png)

#### Dim_Pilot Table
![pilot_dim](assets/dim_pilot.png)

#### Dim_Date Table
![date_dim](assets/dim_date.png)

### Row Level Security Policy on Secure view based on fact table
#### ACCOUNTADMIN/SYSADMIN ROLE
![secure_admin](assets/secure_admin.png)
#### GENERAL_ANALYST ROLE
![secure_general_analyst](assets/secure_general_analyst.png)
#### OPS_ANALYST ROLE
![secure_ops_analyst](assets/secure_ops_analyst.png)
