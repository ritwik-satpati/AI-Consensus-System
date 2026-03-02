# ai_custom_prompt_orchestrator.py

from functions.ai_provider_mapper import mapping_ai_provider
from functions.log_generator import write_log

# Map provider name to its corresponding function
provider_map = mapping_ai_provider()

# This function runs all configured models with custom promt and collects their outputs
def run_models_with_custom_prompts(prompts_with_model, models_data, request_id, min_required_models=1):
    """
    prompts_with_model => {model_name : prompt}
    This function runs all configured models with custom promt and collects their outputs
    Returns => [{model_name : output}]
    """

    # Updating log entry
    write_log(filename=request_id, message="AI_CUSTOM_PROMPT_ORCHESTRATOR | START | Executing models with custom prompts")

    outputs = []

    # Validation
    if len(prompts_with_model) < min_required_models:
        
        # Updating log entry
        write_log(filename=request_id, message=f"AI_CUSTOM_PROMPT_ORCHESTRATOR | FAILED | Provided prompts = {len(prompts_with_model)} | Required = {min_required_models}")
        write_log(filename=request_id, message=f"ERROR : At least {min_required_models} models required for AI Consensus. Provided = {len(models_data)}")

        raise ValueError(f"At least {min_required_models} models required. Provided = {len(prompts_with_model)}")

    # Build model lookup dictionary
    model_config_map = {
        model_data["model"]: model_data
        for model_data in models_data
    }

    # Execute each model with its own prompt
    for model_name, prompt in prompts_with_model.items():

        if model_name not in model_config_map:
            
            # Updating log entry
            write_log(filename=request_id, message=f"AI_CUSTOM_PROMPT_ORCHESTRATOR | FAILED | Model config not found | {model_name}")
            write_log(filename=request_id, message=f"ERROR : Model config not found = {model_name}")
            
            continue

        model_data = model_config_map[model_name]
        company = model_data["company"].lower()
        key = model_data["key"]

        if company in provider_map:

            result = provider_map[company](
                prompt=prompt,
                model=model_name,
                key=key,
                request_id=request_id
            )

            outputs.append(result)
            
            # Updating log entry
            write_log(filename=request_id, message=f"AI_CUSTOM_PROMPT_ORCHESTRATOR | SUCCESS | Output added | {company} | {model_name}")

        else:
            
            # Updating log entry
            write_log(filename=request_id, message=f"AI_CUSTOM_PROMPT_ORCHESTRATOR | FAILED | Failed to add | {company}")
            write_log(filename=request_id, message=f"ERROR : Unsupported provider = {company}")

    # Updating log entry
    write_log(filename=request_id, message=f"AI_CUSTOM_PROMPT_ORCHESTRATOR | SUCCESS | Completed execution for {len(outputs)} models")

    return outputs