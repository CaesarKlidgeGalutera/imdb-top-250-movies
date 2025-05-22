from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def test():
    print("Test")
    
p_upload = PythonOperator(
    task_id = 'test',
    python_callable= test,
    op_kwargs = {}
)


upload = BashOperator(
    task_id='scrape_data',
    bash_command='scraper.py'
)


upload

