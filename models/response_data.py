# response_data.py
MODULE_NAME = "RESPONSE_DATA"

# Import modules
from functions.time_utils import get_current_time


def get_response_data(model_id, provider_name, input, output=None, p_tokens=0, c_tokens=0, status="success", error=None):
    """
    Creates structured response dictionary for ai model api call output.
    """

    return {
        "model": model_id,
        "provider": provider_name,
        "input": input,
        "output": output,
        "prompt_token": p_tokens,
        "completion_token": c_tokens,
        "status": status,
        "error": error,
        "created_at": get_current_time()
    }