from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from data_ingress import fetch_data
from process_data import process_data
from data_store import store_data

default_args = {
    'owner': 'data_team',
    'start_date': datetime(2023, 10, 13),
    'retries': 1,
    'retry_delay': timedelta(minutes=5), 
}

dag = DAG(
    'DataBridgeDAG',
    default_args=default_args,
    description='A DAG to load data from a REST API, process, and store it in a database',
    schedule_interval=timedelta(seconds=1200),
    catchup=False,
)

data_ingress_task = PythonOperator(
    task_id='data_ingress',
    python_callable=fetch_data,
    dag=dag,
)

process_data_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    op_args=[data_ingress_task.output],
    provide_context=True,
    dag=dag,
)

data_store_task = PythonOperator(
    task_id='data_store',
    python_callable=store_data,
    op_args=[process_data_task.output],
    provide_context=True,
    dag=dag,
)

data_ingress_task >> process_data_task >> data_store_task
