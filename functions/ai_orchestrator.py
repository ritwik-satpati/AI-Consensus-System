# ai_orchestrator.py
MODULE_NAME = "AI_ORCHESTRATOR"

import asyncio

from functions.ai_provider_mapper import mapping_ai_provider
from functions.log_generator import write_log

# Map provider name to its corresponding function
provider_map = mapping_ai_provider()

# This function runs all configured models with single or custom prompt and collects their outputs
async def run_models( models_data, system_prompt, request_id, prompt=None, prompts_with_model=None, min_required_models=1):
    """
    prompt (for single prompt for all model)
    prompts_with_model => {model_name : prompt}
    This function runs all configured models with  single or custom prompt and collects their outputs
    Returns => [{model_name : output}]
    """

    outputs = []
    tasks = []
    
    # When only one prompt is received
    if prompt and not prompts_with_model:
        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Single prompt execution started")

        prompts_with_model = {
            model_data["model"]: prompt
            for model_data in models_data
        }

        min_required_models=2

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Single prompt coverted to Custom prompt")
    else :
        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Custom prompt execution started")

    # Validation
    if not prompts_with_model:
        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Both prompt & prompts_with_model are not there")
        write_log(filename=request_id, message=f"ERROR : Either prompt or prompts_with_model must be provided")

        raise ValueError("Either prompt or prompts_with_model must be provided")

    # Validation
    if len(prompts_with_model) < min_required_models:
        
        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Provided prompts = {len(prompts_with_model)} | Required = {min_required_models}")
        write_log(filename=request_id, message=f"ERROR : At least {min_required_models} models required for AI Consensus. Provided = {len(models_data)}")

        raise ValueError(f"At least {min_required_models} models required. Provided = {len(prompts_with_model)}")

    # Build model lookup dictionary
    model_config_map = {
        model_data["model"]: model_data
        for model_data in models_data
    }

    # Execute each model with its own prompt
    for model_name, model_prompt in prompts_with_model.items():

        if model_name not in model_config_map:
            
            # Updating log entry
            write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Model config not found | {model_name}")
            write_log(filename=request_id, message=f"ERROR : Model config not found = {model_name}")
            
            continue

        model_data = model_config_map[model_name]
        model_provider = model_data["provider"].lower()
        model_key = model_data["key"]

        if model_provider in provider_map:

            # Create async task
            task = provider_map[model_provider](
                prompt=model_prompt,
                model=model_name,
                key=model_key,
                system_prompt=system_prompt,
                request_id=request_id
            )

            tasks.append(task)

            # Updating log entry
            write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Task created | {model_provider} | {model_name}")

        else:
            
            # Updating log entry
            write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Failed to add | {model_provider}")
            write_log(filename=request_id, message=f"ERROR : Unsupported provider = {model_provider}")
        
    # Run all tasks concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Process results
    for result in results:
        
        if isinstance(result, Exception):
            
            # Updating log entry
            write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Model execution error | {str(result)}")
            write_log(filename=request_id, message=f"ERROR : {str(result)}")

        else:
            
            outputs.append(result)
            
            # Updating log entry
            write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Output added | {result["provider"]} | {result["model"]}")


    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Completed execution for {len(outputs)} models")

    return outputs