from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import json
from pymongo import MongoClient
import logging

API_ENDPOINT = 'http://api_server/api/products'
mongo_conn_str = 'mongodb://mongo:27017/'

default_args = {
    'owner': 'data_team',
    'start_date': datetime(2023, 10, 13),
    'retries': 1,
    'retry_delay': timedelta(minutes=5), 
}


def data_ingress():
    try:
        response = requests.get(API_ENDPOINT, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        api_data = response.json()
        return api_data
    except Exception as e:
        logging.error(f"Error occurred while calling API: {e}")
        return None

def process_data(**kwargs):
    ti = kwargs['ti']
    api_data = ti.xcom_pull(task_ids='data_ingress')  
    if api_data is not None:
        processed_data = [process_record(record) for record in api_data]
        return processed_data
    else:
        return None

def process_record(record):
    record['ins_dt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return record

def data_store(**kwargs):
    ti = kwargs['ti']
    processed_data = ti.xcom_pull(task_ids='process_data')  
    if processed_data is not None:
        try:
            client = MongoClient(mongo_conn_str) 
            db = client['products_database']
            collection = db['products']

            for record in processed_data:
                collection.insert_one(record)

            client.close()
            logging.info("Data stored in MongoDB successfully.")
        except Exception as e:
            logging.error(f"Error occurred while storing data in MongoDB: {e}")

dag = DAG(
    'DataBridgeDAG',
    default_args=default_args,
    description='A DAG to load data from a REST API, process, and store it in a database',
    schedule_interval=timedelta(seconds=1200),
    catchup=False,
)

data_ingress_task = PythonOperator(
    task_id='data_ingress',
    python_callable=data_ingress,
    dag=dag,
)

process_data_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    provide_context=True,
    dag=dag,
)

data_store_task = PythonOperator(
    task_id='data_store',
    python_callable=data_store,
    provide_context=True,
    dag=dag,
)

data_ingress_task >> process_data_task >> data_store_task
