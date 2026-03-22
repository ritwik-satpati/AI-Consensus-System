# prompt_manager.py
MODULE_NAME = "PROMPT_MANAGER"

from functions.log_generator import write_log


def get_prompt(request_id):
    """
    This function returns a hardcoded prompt
    """
    
    prompt = "Explain API in simple words within 100 words"
    
    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Base Prompt loaded")

    return prompt