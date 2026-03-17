# token_data.py
MODULE_NAME = "TOKEN_DATA"

def get_token_data(stage_name, model, provider, prompt_token=0, completion_token=0, other_token=0):
    """
    Creates structured token usage dictionary for a given stage and model.
    """
    
    return {
        "stage": stage_name,
        "model": model,
        "provider": provider,
        "prompt_token": prompt_token,
        "completion_token": completion_token,
        "other_token": other_token,
        "total_token": prompt_token + completion_token + other_token
    }