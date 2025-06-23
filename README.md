# 🧠 Threat-Enriched Log Pipeline

This project demonstrates how to build a lightweight, Python-based data pipeline for enriching and forwarding security logs. Designed to simulate a real-world detection engineering workflow, this pipeline extracts log data from a SQL database, enriches IP addresses using VirusTotal threat intelligence, and sends the structured results to a syslog-compatible SIEM (e.g., Splunk).

---

## 🚀 Overview

**Pipeline Flow:**
1. **SQL Extraction**: Pulls unprocessed web application logs from a Microsoft SQL Server database.
2. **Checkpointing**: Tracks the last processed `log_id` using a JSON file to ensure only new data is processed.
3. **Enrichment**:
   - Counts IP occurrences in the dataset.
   - Enriches IPs with VirusTotal data (malicious score, ASN, country, etc.).
4. **Output**: Forwards enriched logs to Splunk (or any syslog listener) in JSON format.

---

## 📁 Project Structure

.
├── main.py # Entry point for executing the pipeline
├── functions/
│ ├── sql_extract.py # SQL fetch logic & DB abstraction
│ ├── enrich.py # IP enrichment logic
│ ├── send_logs.py # Syslog output module
│ ├── utils.py # Checkpoint file management
│ └── Virus_Total_API.py # VirusTotal API integration
├── config/
│ └── checkpoint.json # Tracks last processed log_id

---

## ⚙️ Setup Instructions

### 1. Prerequisites
- Python 3.9+
- Local Microsoft SQL Server (with `web_application` table)
- Splunk or any syslog-compatible listener
- VirusTotal API key

### 2. Install Dependencies
```bash
pip install pyodbc requests
3. Set Environment Variable
bash
Copy
Edit
export VT_API_KEY="your_virustotal_api_key"
4. Create Database Table
sql
Copy
Edit
CREATE TABLE dbo.web_application (
    log_id INT PRIMARY KEY IDENTITY,
    timestamp DATETIME,
    ip_address VARCHAR(45),
    resource NVARCHAR(MAX),
    query NVARCHAR(MAX)
);
Populate this table with sample or real log data.

5. Run the Pipeline
bash
Copy
Edit
python main.py
Logs will be enriched and forwarded to 127.0.0.1:514 over UDP as JSON.

📌 Notes
The VirusTotal API has a public request limit (4 requests/min); the script includes a time.sleep(15) to avoid throttling.

This project is intentionally modular. You can easily swap the enrichment provider, change the data source, or update the output destination.

Checkpointing ensures the pipeline is idempotent and only processes new entries.

💡 Why This Matters
This project bridges operational and strategic skills in detection engineering:

Writing Python pipelines for real-world SOC needs

Integrating open-source threat intelligence

Designing safe, stateful ETL logic

Demonstrating both GRC awareness and technical fluency

🧑‍💻 Author
Eric Passeno
CISSP | Detection Engineer | Security Automation Enthusiast
📁 eric-cyber.com
🐙 GitHub

