import requests
import os


VT_API = os.getenv('VT_API_KEY')
def VT_API_IP_Report(ip_address):
    """
    Queries the VirusTotal API for an IPv4 address report.
    Returns a dictionary of extracted threat intelligence, or None on failure.
    """

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {"x-apikey": VT_API}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return parse_vt_ip_response(response.json())
    else:
        print(f"[VT_API] Error {response.status_code}: {response.text}")
        return None


def parse_vt_ip_response(passed_report):
    """
    Parses a VirusTotal IP report and extracts relevant fields.
    Returns a dictionary with summary threat data and network details.
    """

    attributes = passed_report.get('data', {}).get('attributes', {})

    Report = {
        'Malicious_Score': attributes.get('last_analysis_stats', {}).get('malicious'),
        'Harmless_Score': attributes.get('last_analysis_stats', {}).get('harmless'),
        'Suspicious_Score': attributes.get('last_analysis_stats', {}).get('suspicious'),
        'Undetected_Score': attributes.get('last_analysis_stats', {}).get('undetected'),

        'ASN': attributes.get('asn'),
        'Country': attributes.get('country'),
        'Network': attributes.get('network'),
        'Regional_Internet_Registry': attributes.get('regional_internet_registry'),

        'First_Seen': attributes.get('first_seen'),
        'Last_Modified': attributes.get('last_modification_date'),

    }
    return Report



