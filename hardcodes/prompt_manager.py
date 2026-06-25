# prompt_manager.py
MODULE_NAME = "PROMPT_MANAGER"

from functions.log_generator import write_log


def get_prompt(request_id):
    """
    This function returns a hardcoded prompt
    """

    try:
        import os
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, "prompt.txt")

        with open(file_path, "r", encoding="utf-8") as f:
            prompt = f.read().strip()

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Base Prompt loaded")
        
        return prompt
 
    except Exception as e:
        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Base Prompt not loaded")
        write_log(filename=request_id, message=f"ERROR : {str(e)}")
        return None