# response_logger.py

# Import modules
import json
import os
from functions.time_utils import get_current_time
from functions.log_generator import write_log

# This function saves AI response data into a JSON log file
def save_response_log(request_id, outputs, dir, prompt = None):

    # Ensure logs directory exists
    os.makedirs(dir, exist_ok=True)

    # Define dynamic filename
    filename = f"{dir}/{request_id}.json"

    # Structure the data to be saved
    data = {
        "request_id": request_id,
        "input": prompt,
        "outputs": outputs,
        "status": "success",
        "created_at": get_current_time()
    }

    # Write JSON file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    # Updating log entry 
    write_log(filename=request_id, message=f"RESPONSE_LOGGER | SUCCESS | Response log saved | {filename}")

    return data