# request_id_generator.py

# Import modules
from functions.time_utils import get_current_time
from functions.log_generator import write_log

# This function generates a unique request ID using current timestamp
def generate_request_id(pre_log_messages = []):
    time = get_current_time()

    base = time.split(" ")[0] + " " + time.split(" ")[1]  # remove timezone
    request_id = base.replace("-", "").replace(":", "").replace(" ", "_").replace(".", "_")

    # Updating log entry 
    if len(pre_log_messages) > 0 :
        for pre_log_message in pre_log_messages:
            write_log(filename=request_id, message=f"{pre_log_message}", current_time=time)

    # write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM | START | AI_CONSENSUS_SYSTEM", current_time=time)
    write_log(filename=request_id, message=f"REQUEST_ID_GENERATOR | SUCCESS | Request Id generated | {request_id}", current_time=time)

    # Format: YYYYMMDD_HHMMSS
    # return datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    return request_id