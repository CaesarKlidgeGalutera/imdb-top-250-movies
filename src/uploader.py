import boto3
import os
import json
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3')

bucket_name = os.getenv('bucket_name')

file_path = '../data/raw/data.json'

with open(file_path, 'r') as file:
    data = json.load(file)
    
file_name = f"imdb-top-250-movies-{data["scraped_at"]}"

s3.put_object(
    Bucket=bucket_name,
    Key=file_name,
    Body=file_path,
    ContentType='application/json'
)