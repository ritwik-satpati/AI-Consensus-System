# token_summary_generator.py

import json
import os
from models.token_data import get_token_data
from functions.log_generator import write_log


def generate_token_summary( request_id, stage1_output_data, stage2_output_data, stage3_output_data, directory):
    """
    Generates token summary JSON as array of objects.

    Each object contains:
    stage, model, prompt_token, completion_token, other_token, total_token
    """

    os.makedirs(directory, exist_ok=True)

    stage_map = {
        "STAGE_1": stage1_output_data,
        "STAGE_2": stage2_output_data,
        "STAGE_3": stage3_output_data
    }

    result = []

    # Grand totals across all stages & all models
    grand_totals = {
        "prompt_token": 0,
        "completion_token": 0,
        "other_token": 0
    }

    # Model-wise totals across ALL stages
    model_grand_totals = {}

    # Loop through each stage
    for stage_name, stage_data in stage_map.items():

        stage_token_map = {}

        # Loop through outputs inside stage
        for output in stage_data or []:

            model = output.get("model")

            if model not in stage_token_map:
                stage_token_map[model] = {
                    "prompt_token": 0,
                    "completion_token": 0,
                    "other_token": 0
                }

            stage_token_map[model]["prompt_token"] += output.get("prompt_token", 0) or 0
            stage_token_map[model]["completion_token"] += output.get("completion_token", 0) or 0
            stage_token_map[model]["other_token"] += output.get("other_token", 0) or 0


        # Process stage-level aggregation
        for model, tokens in stage_token_map.items():

            # Update overall grand totals
            grand_totals["prompt_token"] += tokens["prompt_token"]
            grand_totals["completion_token"] += tokens["completion_token"]
            grand_totals["other_token"] += tokens["other_token"]

            # Update model-level grand totals
            if model not in model_grand_totals:
                model_grand_totals[model] = {
                    "prompt_token": 0,
                    "completion_token": 0,
                    "other_token": 0
                }

            model_grand_totals[model]["prompt_token"] += tokens["prompt_token"]
            model_grand_totals[model]["completion_token"] += tokens["completion_token"]
            model_grand_totals[model]["other_token"] += tokens["other_token"]

            # Add stage-level summary
            result.append(
                get_token_data(
                    stage_name=stage_name,
                    model=model,
                    prompt_token=tokens["prompt_token"],
                    completion_token=tokens["completion_token"],
                    other_token=tokens["other_token"]
                )
            )

            # Updating log entry
            write_log( filename=request_id, message=f"TOKEN_SUMMARY_GENERATOR | SUCCESS | Token summary added | {stage_name} | {model}")


    # Add ALL_STAGES summary per model
    for model, tokens in model_grand_totals.items():

        result.append(
            get_token_data(
                stage_name="ALL_STAGES",
                model=model,
                prompt_token=tokens["prompt_token"],
                completion_token=tokens["completion_token"],
                other_token=tokens["other_token"]
            )
        )

        # Updating log entry
        write_log(filename=request_id, message=f"TOKEN_SUMMARY_GENERATOR | SUCCESS | Token summary added | ALL_STAGES | {model}")


    # Add global ALL_STAGES + ALL_MODELS summary
    result.append(
        get_token_data(
            stage_name="ALL_STAGES",
            model="ALL_MODELS",
            prompt_token=grand_totals["prompt_token"],
            completion_token=grand_totals["completion_token"],
            other_token=grand_totals["other_token"]
        )
    )

    # Updating log entry
    write_log( filename=request_id, message=f"TOKEN_SUMMARY_GENERATOR | SUCCESS | Token summary added | ALL_STAGES | ALL_MODELS")

    output_path = f"{directory}/{request_id}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    # Updating log entry
    write_log( filename=request_id, message=f"TOKEN_SUMMARY_GENERATOR | SUCCESS | Token summary generated | {output_path}")

    return result