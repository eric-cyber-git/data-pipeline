from functions.sql_extract import fetch_new_logs
from functions.utils import load_checkpoint, update_checkpoint
from functions.enrich import enrich_logs
from functions.send_logs import send_logs

def main():
    """
    Main pipeline entry point:
    - Loads checkpoint
    - Pulls new logs from SQL
    - Enriches with hit count + VirusTotal threat intel
    - Updates checkpoint
    - Forwards results to Splunk via syslog
    """
    last_seen_id = load_checkpoint()
    new_logs = fetch_new_logs(last_seen_id)

    if not new_logs:
        print("No new logs to process.")
        return

    enriched_logs = enrich_logs(new_logs)

    latest_id = max(log["log_id"] for log in new_logs)
    update_checkpoint(latest_id)

    send_logs(enriched_logs)

if __name__ == "__main__":
    main()