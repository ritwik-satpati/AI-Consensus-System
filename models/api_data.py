# api_data.py

def get_api_data(company_name, model_id, api_key):

    return {
        "company": company_name,
        "model": model_id,
        "key": api_key
    }