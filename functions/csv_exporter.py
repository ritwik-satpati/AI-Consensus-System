# csv_exporter.py
MODULE_NAME = "CSV_EXPORTER"

# Import modules
import os
import pandas as pd
from functions.log_generator import write_log


def export_csv(request_id, data, dataframe_label=None, isPrint=False, directory=None):
    """
    This function exports given data into a CSV file.

    Parameters:
    request_id   : str  -> Unique request identifier
    data         : list[dict] | dict | pandas.DataFrame
    output_label : str  -> Optional label for console print
    directory    : str  -> Output directory

    Returns:
    str | None -> Path of saved file (if saved), else None
    """

    # Convert to DataFrame if not already
    if not isinstance(data, pd.DataFrame):
        df = pd.DataFrame(data)
    else:
        df = data

    # Print Dataframe if output_label is there
    if dataframe_label and isPrint:
        print(f"{dataframe_label} :\n{df}")
        
        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Dataframe printed | {dataframe_label}")


    # Save output file in different directory if directory is mentioned 
    if directory:
        # Ensure structured folder exists
        os.makedirs(directory, exist_ok=True)

        # Generate filename
        filename = f"{directory}/{request_id}.csv"

        # Export to CSV
        df.to_csv(filename, index=False)

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | CSV file created | {filename}")

    return