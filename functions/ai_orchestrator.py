# ai_orchestrator.py

from functions.ai_provider_mapper import mapping_ai_provider
from functions.log_generator import write_log

# Map provider name to its corresponding function
provider_map = mapping_ai_provider()

# This function runs all configured models and collects their outputs
def run_models(prompt, models_data, request_id, min_required_models=2):

    outputs = []  # Store results from each provider


    if len(models_data) < min_required_models:
        # Updating log entry 
        write_log(filename=request_id, message=f"AI_ORCHESTRATOR | FAILED | Provided models = {len(models_data)} | Required models = {min_required_models}")
        write_log(filename=request_id, message=f"ERROR : At least {min_required_models} models required for AI Consensus. Provided = {len(models_data)}")

        raise ValueError("At least {min_required_models} models required for AI Consensus. Provided = {len(models_data)}")

    # Loop through each model configuration
    for model_data in models_data:
        
        company = model_data["company"].lower()  # Provider name
        model_id = model_data["model"]           # Model identifier
        key = model_data["key"]                  # API key

        # Check if provider is supported
        if company in provider_map:

            # Call the appropriate provider function
            result = provider_map[company](
                prompt=prompt,
                model=model_id,
                key=key,
                request_id=request_id
            )

            outputs.append(result)  # Save result

            # Updating log entry 
            write_log(filename=request_id, message=f"AI_ORCHESTRATOR | SUCCESS | Output added | {company} | {model_id}")

        else:
            # Updating log entry 
            write_log(filename=request_id, message=f"AI_ORCHESTRATOR | FAILED | Failed to add | {company}")
            write_log(filename=request_id, message=f"Error : Unsupported provider = {company}")

    return outputs  # Return all collected outputs