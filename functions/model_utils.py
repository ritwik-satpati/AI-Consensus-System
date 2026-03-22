# model_utils.py
MODULE_NAME = "MODEL_UTILS"


def get_safe_models(request_id, models):
    """
    This function returns a safe copy of model configurations.
    It masks sensitive fields like API keys before saving/logging.
    """
    
    from functions.security_utils import mask_key
    from functions.log_generator import write_log

    safe_models = []

    for model in models:

        # Create a shallow copy to avoid modifying original data
        safe_model = model.copy()

        # Mask API key if present
        if "key" in safe_model:
            safe_model["key"] = mask_key(request_id=request_id, key=safe_model["key"])

        # Append safe model to list
        safe_models.append(safe_model)

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | API Key masked | {model.get("provider")} | {model.get("model")}")

    
    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | All {len(models)} API Keys masked")


    return safe_models