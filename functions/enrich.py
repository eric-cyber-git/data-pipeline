from functions.sql_extract import fetch_new_logs
from functions.utils import load_checkpoint, update_checkpoint
from functions.enrich import enrich_logs
from functions.send_logs import send_logs


last_seen_id = load_checkpoint()
SQL_Logs= fetch_new_logs(last_seen_id)

if SQL_Logs:

    # Enrich the data returned from SQL
    enriched_logs = enrich_logs(SQL_Logs)

    # Update config file
    last_id = max(log["log_id"] for log in SQL_Logs)
    update_checkpoint(last_id)

    # Forward enriched data to Splunk 
    send_logs(enriched_logs)
else:
    print("No new logs to process.")




