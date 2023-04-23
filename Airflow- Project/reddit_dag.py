from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from reddit_etl import run_reddit_etl

#  default configuration options for the DAG
default_args = {
	'owner': 'airflow',
	'depends_on_past': False, #Whether or not the DAG should consider past runs when determining if the current run should be executed.
	'start_date': datetime(2020, 11, 8), #The date and time when the DAG should start running
	'email': ['airflow@example.com'], #A list of email addresses that should receive notifications about the DAG's execution.
	'email_on_failure': False, #Whether or not to send an email notification if the DAG fails.
	'email_on_retry': False, #same but for retried
	'retries': 1, #The number of times to retry the DAG if it fails
	'retry_delay': timedelta(minutes=1) #The amount of time to wait before retrying the DAG if it fails
}

dag = DAG(
	'reddit_dag', #The name of the DAG
	default_args=default_args, #Passing the default_args dictionary to the DAG constructor
	description='A simple ETL DAG',
)

run_etl = PythonOperator(
	task_id='complete_reddit_etl', #name of the task
	python_callable=run_reddit_etl, #the function that will be executed
	dag=dag, #Passing the dag instance to the PythonOperator constructor
)