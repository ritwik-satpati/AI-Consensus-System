# csv_exporter.py
MODULE_NAME = "CSV_EXPORTER"

# Import modules
import os
import pandas as pd
from functions.log_generator import write_log


# This function converts data into CSV file
def export_csv(request_id, data, directory):
    """
    Exports given data (list/dict/DataFrame) into CSV file.

    Parameters:
    request_id : Unique request identifier
    data       : Data to export (list of dict OR pandas DataFrame)
    directory  : Output directory
    """

    # # Updating log entry
    # write_log(filename=request_id, message=f"{MODULE_NAME} | START | CSV export initiated")

    # Ensure directory exists
    os.makedirs(directory, exist_ok=True)

    # Convert to DataFrame if not already
    if not isinstance(data, pd.DataFrame):
        df = pd.DataFrame(data)
    else:
        df = data

    # Generate filename
    filepath = f"{directory}/{request_id}.csv"

    # Export to CSV
    df.to_csv(filepath, index=False)

    # # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | CSV file created | {filepath}")

    return filepath