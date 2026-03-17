# scoring_prompt_orchestrator.py
MODULE_NAME = "SCORING_PROMPT_ORCHESTRATOR"

from functions.scoring_prompt_builder import build_scoring_prompt
from functions.log_generator import write_log


def build_scoring_prompt_orchestrator(request_id, original_prompt, model_outputs, random_map):
    """
    random_map => {evaluator_model : candidate_model}
    model_output => {candidate_model : candidate_model_answer}
    Returns => {evaluator_model : scoring_prompt_for_candidate_model}
    """

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | START | Building scoring prompts")

    scoring_prompts = {}

    # Loop through evaluator → candidate mapping
    for evaluator_model, candidate_model in random_map.items():

        # Ensure candidate exists in model_outputs
        if candidate_model not in model_outputs:

            # Updating log entry
            write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Candidate model output missing | {candidate_model}")
            write_log(filename=request_id, message=f"ERROR : Candidate model output missing = {candidate_model}")

            continue

        # Get candidate's answer
        candidate_answer = model_outputs[candidate_model]

        # Build scoring prompt
        scoring_prompt = build_scoring_prompt(
            original_prompt=original_prompt,
            model=candidate_model,
            answer=candidate_answer,
            request_id=request_id
        )

        # Store prompt under evaluator model
        scoring_prompts[evaluator_model] = scoring_prompt

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Evaluator Model = {evaluator_model} | Candidate Model = {candidate_model}")

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Generated {len(scoring_prompts)} scoring prompts")
    
    return scoring_prompts