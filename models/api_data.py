# api_data.py
MODULE_NAME = "API_DATA"

def get_api_data(provider_name, model_id, api_key):

    return {
        "provider": provider_name,
        "model": model_id,
        "key": api_key
    }