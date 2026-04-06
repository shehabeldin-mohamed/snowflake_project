from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

with DAG(
    dag_id='snowflake_airline_etl',
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['snowflake']
) as dag:

    with TaskGroup(group_id='bronze_ingestion_group') as bronze_group:

        load_bronze_data = SQLExecuteQueryOperator(
            task_id='load_bronze_data',
            conn_id='snowflake_default',
            sql="CALL BRONZE.LOAD_RAW_DATA();",
            autocommit=True
        )

        archive_files = SQLExecuteQueryOperator(
            task_id='archive_bronze_files',
            conn_id='snowflake_default',
            sql="CALL BRONZE.ARCHIVE_FILES();",
            autocommit=True
        )

        cleanup_incoming_stage = SQLExecuteQueryOperator(
            task_id='cleanup_incoming_stage',
            conn_id='snowflake_default',
            sql="CALL BRONZE.CLEANUP_INCOMING_STAGE();",
            autocommit=True
        )

        load_bronze_data >> archive_files >> cleanup_incoming_stage


    load_silver_data = SQLExecuteQueryOperator(
        task_id='load_silver_data',
        conn_id='snowflake_default',
        sql="CALL SILVER.LOAD_CLEAN_DATA();",
        autocommit=True
    )

    load_gold_data = SQLExecuteQueryOperator(
        task_id='load_gold_data',
        conn_id='snowflake_default',
        sql="CALL GOLD.LOAD_STAR_SCHEMA();",
        autocommit=True
    )

    bronze_group >> load_silver_data >> load_gold_data
