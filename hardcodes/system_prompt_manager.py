# system_prompt_manager.py
MODULE_NAME = "SYSTEM_PROMPT_MANAGER"

from functions.log_generator import write_log

# This function returns a hardcoded prompt
def get_system_prompt(request_id):
    prompt = "You are a helpful assistant."
    
    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Base System Prompt loaded")

    return prompt