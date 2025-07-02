"""
Backblaze B2 bucket downloader.

Downloads all objects from a private B2 bucket using S3-compatible API,
preserving the original folder structure.
"""

import os
import boto3
from dotenv import load_dotenv

# === Load environment variables ===
load_dotenv()

B2_KEY_ID = os.getenv("B2_KEY_ID")
B2_APP_KEY = os.getenv("B2_APP_KEY")
B2_BUCKET_NAME = os.getenv("B2_BUCKET_NAME")
B2_ENDPOINT_URL = os.getenv("B2_ENDPOINT_URL")
LOCAL_DOWNLOAD_DIR = os.getenv("LOCAL_DOWNLOAD_DIR", "./b2_download")

session = boto3.session.Session()
s3 = session.client(
    service_name="s3",
    endpoint_url=B2_ENDPOINT_URL,
    aws_access_key_id=B2_KEY_ID,
    aws_secret_access_key=B2_APP_KEY
)


def download_all_files():
    """
    Download all objects from the configured Backblaze B2 bucket.

    Uses the S3-compatible API to list and download all files,
    preserving the original folder structure under the local target directory.

    :raises ClientError: If an error occurs during download.
    """
    paginator = s3.get_paginator('list_objects_v2')
    total = 0

    for page in paginator.paginate(Bucket=B2_BUCKET_NAME):
        if 'Contents' not in page:
            continue

        for obj in page['Contents']:
            key = obj['Key']
            local_path = os.path.join(LOCAL_DOWNLOAD_DIR, key)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)

            print(f"Downloading: {key} -> {local_path}")
            s3.download_file(B2_BUCKET_NAME, key, local_path)
            total += 1

    print(f"✅ Download complete. Total files: {total}")


if __name__ == "__main__":
    # Entry point for standalone execution.
    # Downloads all files from the B2 bucket to the local folder.
    download_all_files()
