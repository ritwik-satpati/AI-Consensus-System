# output_manager.py
MODULE_NAME = "OUTPUT_MANAGER"

import json
import os
from functions.time_utils import get_current_time
from functions.log_generator import write_log


def update_output_file(request_id, stage_name, stage_data, directory="outputs"):
    """
    This function updates a single pipeline output JSON file incrementally
    """

    # Ensure output directory exists
    os.makedirs(directory, exist_ok=True)

    # Define dynamic filename
    file_path = f"{directory}/{request_id}.json"

    # Load existing data if file exists
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            # Fallback if file is corrupted
            data = {
                "request_id": request_id,
                "stages": {},
                "createdAt": get_current_time(),
            }
    else:
        data = {
            "request_id": request_id,
            "stages": {},
            "createdAt": get_current_time(),
        }

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Output file created | {file_path}")

    # Ensure stages key exists
    if "stages" not in data:
        data["stages"] = {}

    # Add / update stage data
    data["stages"][stage_name] = stage_data
    data["stages"][stage_name]["savedAt"] = get_current_time()

    # Update last modified timestamp
    data["updatedAt"] = get_current_time()

    # Save updated state
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False, default=str)

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Output file updated | {file_path} | {stage_name}")

    return file_path