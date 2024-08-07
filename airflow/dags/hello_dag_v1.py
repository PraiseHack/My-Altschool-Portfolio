from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    return "Hello world from Airflow! testing again!!"

dag = DAG('hello_world', 
          description='simple tutorial DAG',
          schedule_interval=None,
          start_date= datetime(2023, 1, 1),
          catchup=False)

dummy_operator = EmptyOperator(task_id='dummy_task', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator 