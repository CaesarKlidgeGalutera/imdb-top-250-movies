import boto3
import os
import json
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3')

bucket_name = os.getenv('bucket_name')

file_path = '../data/cleaned/cleaned.json'

with open(file_path, 'r') as file:
    data = json.load(file)
    
file_name = "imdb-top-250-movies"

s3.put_object(
    Bucket=bucket_name,
    Key=file_name,
    Body= json.dumps(data) ,
    ContentType='application/json'
)

print("✅ JSON File is successfully uploaded in S3")