# response_formatter.py

# Import modules
import json
import os
from functions.log_generator import write_log



# This function converts raw AI outputs into structured model-output format
def format_structured_response(request_id, data, dir):

    # Create dictionary: { model_name : model_output }
    result = {item["model"]: item["output"] for item in data["outputs"]}

    # Ensure structured folder exists
    os.makedirs(dir, exist_ok=True)

    # Generate timestamp-based filename
    filename = f"{dir}/{request_id}.json"

    # Save structured result
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    # Updating log entry 
    write_log(filename=request_id, message=f"RESPONSE_FORMATTER | SUCCESS | Structured output saved | {filename}")

    return result