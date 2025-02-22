from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def example_task():
    print("This is an example task.")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='An example DAG for demonstration purposes',
    schedule_interval='@daily',
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

task1 = PythonOperator(
    task_id='example_task',
    python_callable=example_task,
    dag=dag,
)

start >> task1