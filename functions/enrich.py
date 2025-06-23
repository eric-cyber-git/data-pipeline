from functions.virus_total_api import VT_API_IP_Report
from functions.sql_extract import fetch_ip_counts
import time



def enrich_logs(logs):
    """Enriches SQL log records with IP frequency counts and VirusTotal intelligence."""
    
    ip_rows = fetch_ip_counts()
    # Create a map object using dictionary comprehension. 
    ip_hit_map = {row['ip_address']: row['hit_count'] for row in ip_rows}

    enriched = []
    for record in logs:
        ip = record["ip_address"]
        # Update the record with the ip count, if present. If not present, return 1 for count. 
        record["ip_hit_count"] = ip_hit_map.get(ip, 1)
        # Account for VT API Rate Limit of 4 requests per minute
        record.update(VT_API_IP_Report(ip))        
        time.sleep(15)
        enriched.append(record)


    return enriched
