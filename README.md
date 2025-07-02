# Backblaze B2 Downloader

Minimal script to download all files from a private Backblaze B2 bucket using the S3-compatible API, preserving the folder structure.

## 📦 Requirements

- Python 3.12+
- `boto3`
- `python-dotenv`

## ⚙️ Setup

1. Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python download_all.py
```
