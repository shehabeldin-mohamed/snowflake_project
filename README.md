# snowflake_project
This project showcases medallion architecture. The project is done using local airflow setup with snowflake. The pipeline starts by  a csv file into the bronze layer, cleans it and then loads it to the silver layer, and finally to the gold where it is ready for reporting.

## Prerequisites
.env file containing the following: 
* AIRFLOW_UID=50000 
*_PIP_ADDITIONAL_REQUIREMENTS=apache-airflow-providers-snowflake

## Dag
