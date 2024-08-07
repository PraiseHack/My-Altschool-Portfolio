from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta


# define default argument for DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# define the DAG
with DAG(
    'example_task_api_dag',
    default_args=default_args,
    description='An example DAG using task API',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
 ) as dag:
    
    @task
    def hello_task():
        print("Hello world from task API!!")
    
    @task
    def another_hello_task():
        print("Hello world from task API!!")

    # Set task dependencies
    hello_task() >> another_hello_task()
    

        