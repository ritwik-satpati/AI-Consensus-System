# security_utils.py
MODULE_NAME = "SECURITY_UTILS"

# Import modules
from functions.log_generator import write_log


def mask_key(request_id, key):
    """
    This function masks sensitive API keys for safe logging/storage
    """

    start = ""
    end = ""
    masked = ""

    # Return as is if key is empty or too short
    if len(key) <= 2:
        masked = "*" * (len(key))
    
    elif len(key) <= 8:
       # First 3 characters
        start = key[:2]

        # Last 3 characters
        end = key[-2:]

        # Mask middle part
        masked = "*" * (len(key) - 4)
    
    else:
        # First 3 characters
        start = key[:3]

        # Last 3 characters
        end = key[-3:]

        # Mask middle part
        masked = "*" * (len(key) - 6)

    masked_key = f"{start}{masked}{end}"

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Key masked | {masked_key}")

    return masked_key