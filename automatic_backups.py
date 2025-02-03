import os
import time
import glob
import json
import requests
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Variables
confluence_url="https://confluence.mywebsite.com"
personal_token = "<CONFLUENCE-PERSONAL-TOKEN>"
filename_prefix = "full_backup"
skip_attachments = False
keepPermanently = True

# Prepare headers and data
url = "{}/rest/api/backup-restore/backup/site".format(confluence_url)

headers = {
    "Authorization": f"Bearer {personal_token}",
    "Content-Type": "application/json"
}

data = {
    "fileNamePrefix": filename_prefix,
    "keepPermanently": keepPermanently,
    "skipAttachments": skip_attachments
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 200:
    print("Backup initiated successfully.")
    job_id = response.json().get('id')
else:
    print(f"Failed to initiate backup: {response.status_code} - {response.text}")

status_url_template = f"{confluence_url}/rest/api/backup-restore/jobs/{{job_id}}"

# Step 2: Check Backup Status
while True:
    status_url = status_url_template.format(job_id=job_id)
    status_response = requests.get(status_url, headers=headers)

    if status_response.status_code == 200:
        status_data = status_response.json()
        status = status_data.get('jobState')

        # Print Status
        print(f"Current Status: {status}")

        # Check for completion
        if status == "FINISHED":
            print("Backup completed successfully.")
            break
        elif status == "ERROR":
            print("Backup failed.")
            break

        # Sleep before checking again
        time.sleep(5)  # Check every 5 seconds
    else:
        print(f"Failed to check backup status: {status_response.status_code} - {status_response.text}")
        break

# Set the directory path
backup_path = "/var/lib/docker/volumes/confluence_home_data/_data/restore/site/"

# Use glob to get a list of files in the directory
files = glob.glob(os.path.join(backup_path, '*'))

# Check if there are any files in the directory
if files:
    # Find the most recently modified file
    latest_file = max(files, key=os.path.getmtime)
    print("The most recent file is:", latest_file)
else:
    print("No files found in the directory.")


latest_file_name = latest_file.split('/')[-1]

# Send backup tp s3 bucket
# Define your AWS credentials
access_key = '<access-key>'
secret_key = '<secret-key>'
bucket_name = 'service-backups'  # Replace with your bucket name
s3_object_key = 'confluence'  # Specify the path in the bucket
endpoint_url = 'https://<your-s3-endpoint-address>.com'

# Create an S3 client
s3_resource = boto3.resource(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=endpoint_url
)

try:
    s3_resource.Bucket(bucket_name).upload_file(latest_file, f"confluence/{latest_file_name}")
    print(f"Successfully uploaded {latest_file} to {bucket_name}/{latest_file_name}")
except Exception as e:
    print(f"Failed to upload {latest_file} to {bucket_name}: {e}")
