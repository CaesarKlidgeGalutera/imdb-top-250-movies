from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    'owner':'klidge',
    'start_date' : datetime(2025, 5, 23),
    'sla':timedelta(minutes=30),
    'email': 'caesarklidge@gmail.com',
    'email_on_failure': True,
    'email_on_sucess':True
}

imdb_top_250_movies = DAG(
    dag_id ='top_250_movies',
    default_args=default_args,
    schedule_interval= '10 0 * * *') #runs daily at 10am


scrape = BashOperator(
    task_id = 'scrape_date',
    bash_command='scraper.py',
    start_date= datetime(2025, 5, 30),
    dag=imdb_top_250_movies
)

check_raw_data = FileSensor(
    task_id ='check_raw_data',
    filepath= 'C:\Users\caesa\Documents\GitHub\imdb-top-250-movies\data\data.json',
    start_date= datetime(2025, 5, 30),
    mode='reschedule',
    dag=imdb_top_250_movies)

transform = BashOperator(
    task_id= 'transform_raw_data',
    bash_command='transformer.py',
    start_date= datetime(2025, 5, 30),
    dag=imdb_top_250_movies
)

check_cleaned_data= BashOperator(
    
)


scrape >> check_raw_data >> transform

