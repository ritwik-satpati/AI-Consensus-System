# json_exporter.py
MODULE_NAME = "JSON_EXPORTER"

# Import modules
import os
import json
from functions.log_generator import write_log


def export_json(request_id, directory, data, data_label=None):
    """
    This function exports given data into a CSV file.

    Parameters:
    request_id   : str  -> Unique request identifier
    data         : json data
    directory    : str  -> Output directory
    output_label : str  -> Optional label for console print

    Returns:
    str | None -> Path of saved file (if saved), else None
    """

    # Save output file in different directory if directory is mentioned 
    if directory:
    
        # Ensure structured folder exists
        os.makedirs(directory, exist_ok=True)

        # Generate timestamp-based filename
        filename = f"{directory}/{request_id}.json"

        # Save structured result
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | {data_label} outputs saved | {filename}")

    else:
        
        filename = None

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | {data_label} outputs skipped saving")
    
    return filename