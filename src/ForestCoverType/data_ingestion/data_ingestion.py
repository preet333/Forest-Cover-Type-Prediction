import os
import boto3
import pandas as pd
from pathlib import Path
from ForestCoverType import log
from dotenv import load_dotenv

load_dotenv()

# aws_access_key = os.getenv("aws_access_key_id")
# aws_secret_access = os.getenv("aws_secret_access_key")

aws_access_key = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access = os.environ['AWS_SECRET_ACCESS_KEY']


STAGE_NAME = "Data Ingestion Stage"

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_data(self):
        s3 = boto3.resource(service_name='s3', region_name='us-east-1',
                   aws_access_key_id=aws_access_key,
                   aws_secret_access_key=aws_secret_access)
        log.info(f"your aws_access_key={aws_access_key} & aws_secret_key={aws_secret_access}")
        obj = s3.Bucket('forest-cover-type').Object('dataset/data.csv').get()
        
        # s3 = boto3.client('s3', region_name='us-east-1')
        # obj = s3.get_object(Bucket='forest-cover-type', Key='dataset/data.csv')
        

        self.train = pd.read_csv(obj['Body'])
        log.info(f"Downloading Data from s3 Bucket(forest-cover-type)")
        
    def save_data(self):
        data_ingestion_root_dir = Path(self.config['root_dir'])
        train_file = Path(self.config['train_file'])

        train_file_path = os.path.join(data_ingestion_root_dir, train_file)

        self.train.to_csv(train_file_path, index=False)
        log.info(f"data saved successfully at {train_file_path}")

        log.info(f">>>>>>>>>>>>>>>>> {STAGE_NAME} compleated successfully compleated\n")
