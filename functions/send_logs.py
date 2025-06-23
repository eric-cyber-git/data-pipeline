import logging
import logging.handlers
import json

def send_logs(logs):
    """Sends each enriched log record to a local syslog listener (e.g., Splunk)."""

    logger = logging.getLogger("splunk_logger")
    logger.setLevel(logging.INFO)

    syslog_handler = logging.handlers.SysLogHandler(address=('127.0.0.1', 514))  

    # Used to ensure that only syslog payload sent with no meta-data
    syslog_handler.setFormatter(logging.Formatter('%(message)s')) 
    logger.addHandler(syslog_handler)

    # Send each log record as JSON
    for record in logs:
        json_data = json.dumps(record, default=str)
        print(json_data) 
        logger.info(json_data)