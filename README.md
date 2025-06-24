# Threat-Enriched Log Pipeline

This project demonstrates how to build a lightweight, Python-based data pipeline for enriching and forwarding security logs. Designed to simulate a real-world detection engineering workflow, this pipeline extracts log data from a SQL database, enriches IP addresses using VirusTotal threat intelligence, and sends the structured results to a syslog-compatible SIEM (e.g., Splunk).

---

## Overview

**Pipeline Flow:**
1. **SQL Extraction**: Pulls unprocessed web application logs from a Microsoft SQL Server database.
2. **Checkpointing**: Tracks the last processed `log_id` using a JSON file to ensure only new data is processed.
3. **Enrichment**:
   - Counts IP occurrences in the dataset.
   - Enriches IPs with VirusTotal data (malicious score, ASN, country, etc.).
4. **Output**: Forwards enriched logs to Splunk (or any syslog listener) in JSON format.

---

## Project Structure
```
main.py                         # Entry point for executing the pipeline
   Functions/
      -Sql_extract.py           # SQL fetch logic & DB abstraction
      -enrich.py                # IP enrichment logic
      -send_logs.py             # Syslog output module
      -utils.py                 # Checkpoint file management
      -virus_total_ap.py        # VirusTotal API integration
   config/
      -checkpoint.json          # Tracks last processed log_id
```  
---

## Setup Instructions

### 1. Prerequisites
- Python 3.9+
- Local Microsoft SQL Server (with `web_application` table)
- Splunk or any syslog-compatible listener
- VirusTotal API key
- Appropriate ODBC Driver Installed
  

### 2. Install Dependencies
```
pip install pyodbc requests
```
### 3. Set Environment Variable
```
VT_API_KEY="your_virustotal_api_key"
```
### 4. Create Database
   
####4.a Create the database you are going to use when replicating this process
   
####4.b Create the table and fill it with sample data
   ```
sample_data/create_web_application_logs.sql
   ```

####4.c Update the connect string within "sql_extract.py" with your details
   ```
    conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=SERVER-HOSTNAME;"
    "DATABASE=YOU-NEW-Database;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
   ```


### 5. Run the Pipeline
```
python main.py
```
Logs will be enriched and forwarded to 127.0.0.1:514 over UDP as JSON.


# Notes
The VirusTotal API has a public request limit (4 requests/min); the script includes a time.sleep(15) to avoid throttling.

This project is intentionally modular. You can easily swap the enrichment provider, change the data source, or update the output destination.

Checkpointing ensures the pipeline is idempotent and only processes new entries.


# Why This Matters
This project bridges operational and strategic skills in detection engineering:

Writing Python pipelines for real-world SOC needs

Integrating open-source threat intelligence

Designing safe, stateful ETL logic
