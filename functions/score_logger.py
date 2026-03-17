# score_logger.py
MODULE_NAME = "SCORE_LOGGER"

# Import required modules
import json
import os
from functions.log_generator import write_log

# This function saves final score results into a JSON file
def save_scores_log(request_id, scores, dir):

    # Ensure directory exists
    os.makedirs(dir, exist_ok=True)

    # Create filename using request_id
    filename = f"{dir}/{request_id}.json"

    # Structure the score output
    data = scores
        
    # Write JSON file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Score file saved | {filename}")

    return data