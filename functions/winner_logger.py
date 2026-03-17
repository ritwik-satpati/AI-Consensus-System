# score_logger.py
MODULE_NAME = "WINNER_LOGGER"

# Import required modules
import json
import os
from functions.log_generator import write_log


# This function saves final score results into a JSON file
def save_winner_log(request_id, prompt, model, score, output, start_time, end_time, execution_time, dir):

    # Ensure directory exists
    os.makedirs(dir, exist_ok=True)

    # Create filename using request_id
    filename = f"{dir}/{request_id}.json"


    # Structure the score output
    data = {
        "request_id": request_id,
        "prompt": prompt,
        "model": model, 
        "score": score,
        "output": output, 
        "start_time": start_time, 
        "end_time": end_time, 
        "execution_time": execution_time
    }

    # # Print final winner data
    # print(data)
        
    # Write JSON file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Winner file saved | {filename}")


    return data