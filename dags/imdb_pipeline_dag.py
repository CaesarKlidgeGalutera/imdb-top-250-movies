from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime

default_args = {
    'owner':'klidge',
    'start_date' : datetime(2025, 5, 23)
}

imdb_top_250_movies = DAG(dag_id ='top_250_movies', default_args=default_args, schedule_interval= '10 0 * * *') #runs daily at 10am

def test():
    print("Test")
    
p_upload = PythonOperator(
    task_id = 'test',
    python_callable= test,
    op_kwargs = {}
    dag=imdb_top_250_movies
)


upload = BashOperator(
    task_id='scrape_data',
    bash_command='scraper.py',
    dag=p_upload
)


upload >> p_upload

