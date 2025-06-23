import json
import os
from datetime import datetime

CHECKPOINT_FILE = "../config/checkpoint.json"

def load_checkpoint():
    """
    Load the checkpoint file and return the last processed log ID.
    Defaults to 0 if the checkpoint file does not exist.
    """

    if not os.path.exists(CHECKPOINT_FILE):
        return 0 

    with open(CHECKPOINT_FILE, "r") as f:
        data = json.load(f)
        return data.get("last_log_id", 0)

def update_checkpoint(new_log_id):
    """
    Update the checkpoint file with the latest log ID and current timestamp.
    Creates the file path if it does not exist.
    """
    data = {
        "last_log_id": new_log_id,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    os.makedirs(os.path.dirname(CHECKPOINT_FILE), exist_ok=True)

    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(data, f, indent=4)
