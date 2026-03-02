# response_data.py

# Import modules
from functions.time_utils import get_current_time

def get_response_data(model_id, output=None, p_tokens=0, c_tokens=0, status="success", error=None):

    return {
        "model": model_id,
        "output": output,
        "prompt_token": p_tokens,
        "completion_token": c_tokens,
        "status": status,
        "error": error,
        "created_at": get_current_time()
    }