# time_utils.py
MODULE_NAME = "TIME_UTILS"

from datetime import datetime

def get_current_time():
    
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S.%f %z")