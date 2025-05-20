from airflow.operators.bash import BashOperator


upload = BashOperator(
    task_id='scrape_data',
    bash_command='scraper.py'
)


upload

