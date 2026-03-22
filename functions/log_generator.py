# log_generator.py
MODULE_NAME = "LOG_GENERATOR"

import os
from functions.time_utils import get_current_time


def write_log(filename, message, directory="logs", current_time=None):
    """
    Appends a log entry to the specified file.
    
    Each log entry is written in the format:
    YYYY-MM-DD HH:MM:SS    <message>
    
    message >> SERVICE | STATUS | DETAILS
    """

    # If time is not provided, generate fresh timestamp
    if current_time is None:
        current_time = get_current_time()

    # Ensure directory exists
    os.makedirs(directory, exist_ok=True)

    
    # Open file in append mode ("a")
    # If file does not exist, it will be created automatically
    with open(f"{directory}/{filename}.log", "a", encoding="utf-8") as file:
        
        # Write timestamp + tab + message + newline
        file.write(f"{current_time}\t{message}\n")