import pandas 
import numpy
from dotenv import load_dotenv
import os

load_dotenv()
print("Reading Environmental Variables")
aws_access_key=os.getenv("AWS_S3_PACS_ACCESS_KEY")
aws_secret_key=os.getenv("AWS_S3_PACS_SECRET_KEY")
pacs_url=os.getenv("URL")

if (aws_access_key == None) or (aws_secret_key == None):
    print("Failed to access AWS ACCESS KEYS Terminating Program")
    exit(1)
elif pacs_url == None:
    print("Failed to fetch PACS end point, Terminating Program")
    exit(1)
else:
    print("Successfully Retrieved AWS Access Key and PACS endpoint")

def print_env():
    print(aws_access_keys)
    print(aws_secret_key)
