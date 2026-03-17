# token_summary_generator.py
MODULE_NAME = "TOKEN_SUMMARY_GENERATOR"

import json
import os
from models.token_data import get_token_data
from functions.log_generator import write_log


def generate_token_summary(request_id, stage1_output_data, stage2_output_data, stage3_output_data, directory):
    """
    Generates token summary JSON as an array of objects.

    Each object contains:
    stage, model, provider, prompt_token, completion_token, other_token, total_token
    """

    os.makedirs(directory, exist_ok=True)

    stage_map = {
        "STAGE_1": stage1_output_data,
        "STAGE_2": stage2_output_data,
        "STAGE_3": stage3_output_data
    }

    result = []

    # Global totals across all stages
    grand_totals = {
        "prompt_token": 0,
        "completion_token": 0,
        "other_token": 0
    }

    # Model totals across all stages
    model_grand_totals = {}

    # Map model -> provider
    model_provider_map = {}

    # -----------------------------
    # Stage Processing
    # -----------------------------
    for stage_name, stage_data in stage_map.items():

        stage_token_map = {}

        for output in stage_data or []:

            model = output.get("model")
            provider = output.get("provider")

            model_provider_map[model] = provider

            if model not in stage_token_map:
                stage_token_map[model] = {
                    "prompt_token": 0,
                    "completion_token": 0,
                    "other_token": 0
                }

            stage_token_map[model]["prompt_token"] += output.get("prompt_token", 0) or 0
            stage_token_map[model]["completion_token"] += output.get("completion_token", 0) or 0
            stage_token_map[model]["other_token"] += output.get("other_token", 0) or 0

        # -----------------------------
        # Stage-level Aggregation
        # -----------------------------
        for model, tokens in stage_token_map.items():

            provider = model_provider_map.get(model)

            # Update global totals
            grand_totals["prompt_token"] += tokens["prompt_token"]
            grand_totals["completion_token"] += tokens["completion_token"]
            grand_totals["other_token"] += tokens["other_token"]

            # Update model totals
            if model not in model_grand_totals:
                model_grand_totals[model] = {
                    "prompt_token": 0,
                    "completion_token": 0,
                    "other_token": 0
                }

            model_grand_totals[model]["prompt_token"] += tokens["prompt_token"]
            model_grand_totals[model]["completion_token"] += tokens["completion_token"]
            model_grand_totals[model]["other_token"] += tokens["other_token"]

            # Add stage summary
            result.append(
                get_token_data(
                    stage_name=stage_name,
                    model=model,
                    provider=provider,
                    prompt_token=tokens["prompt_token"],
                    completion_token=tokens["completion_token"],
                    other_token=tokens["other_token"]
                )
            )

            # Updating log entry
            write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Token summary added | {stage_name} | {model}")

    # -----------------------------
    # ALL_STAGES per Model
    # -----------------------------
    for model, tokens in model_grand_totals.items():

        provider = model_provider_map.get(model)

        result.append(
            get_token_data(
                stage_name="ALL_STAGES",
                model=model,
                provider=provider,
                prompt_token=tokens["prompt_token"],
                completion_token=tokens["completion_token"],
                other_token=tokens["other_token"]
            )
        )

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Token summary added | ALL_STAGES | {model}")

    # -----------------------------
    # Global Summary
    # -----------------------------
    result.append(
        get_token_data(
            stage_name="ALL_STAGES",
            model="ALL_MODELS",
            provider="ALL_PROVIDERS",
            prompt_token=grand_totals["prompt_token"],
            completion_token=grand_totals["completion_token"],
            other_token=grand_totals["other_token"]
        )
    )

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Token summary added | ALL_STAGES | ALL_MODELS")

    # -----------------------------
    # Save JSON
    # -----------------------------
    output_path = f"{directory}/{request_id}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Token summary generated | {output_path}")

    return result