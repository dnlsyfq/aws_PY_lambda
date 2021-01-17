import pandas as pd
import boto3
import io


bucket = 'analytics-s3-etl-dump' 
file = 'query_EFC2DB.csv'

s3_client = boto3.client('s3')
s3_response_object = s3_client.get_object(Bucket=bucket, Key=file)
object_content = s3_response_object['Body'].read()

def lambda_handler(event, context):
    df = pd.read_csv(io.BytesIO(object_content))
    print(df.head())

