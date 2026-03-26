# stage_validator.py
MODULE_NAME = "STAGE_VALIDATOR"

from functions.log_generator import write_log


def validate_stages(request_id, stages):
    """
    Function to check if all stages are there or not.
    Input => stages : list
    Return => stages_set : list, evaluation_stage : str, scoring_stage : str
    """
    stages_set = set(stages)

    evaluation_stage = ""
    scoring_stage = ""

    all_stages = [
        "SYSTEM_SETUP",
        "INITIAL_EXECUTION",
        # "INITIAL_EXECUTION_RELOAD",
        "CONSENSUS_SYNTHESIS",
        # "CONSENSUS_SYNTHESIS_RELOAD",
        "SCORING_COMBINED",
        # "SCORING_COMBINED_RELOAD",
        "SCORING_RANDOM",
        # "SCORING_RANDOM_RELOAD",
        "SCORE_AGGREGATION",
        "WINNER_SELECTION",
        "REPORT_GENERATION"
    ]

    # Mandatory stages
    mandatory = {
        "SYSTEM_SETUP",
        "INITIAL_EXECUTION",
        "SCORE_AGGREGATION",
        "WINNER_SELECTION",
        "REPORT_GENERATION"
    }

    missing = mandatory - stages_set

    if missing:
        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Missing mandatory stages: {missing}")
        write_log(filename=request_id, message=f"ERROR : Missing mandatory stages: {missing}")
        raise ValueError(f"Missing mandatory stages: {missing}")

    if "CONSENSUS_SYNTHESIS" in stages_set:
        evaluation_stage = "CONSENSUS_SYNTHESIS"
    else:
        evaluation_stage = "INITIAL_EXECUTION"
        all_stages.remove("CONSENSUS_SYNTHESIS")
    
    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | {evaluation_stage} set as evaluation stage")

    # Exactly one of SCORING types
    scoring_group_set = {
        "SCORING_COMBINED",
        "SCORING_RANDOM"
    }

    scoring_stage_set = scoring_group_set & stages_set
    
    if len(scoring_stage_set) != 1:
    
        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Exactly one of SCORING_COMBINED or SCORING_RANDOM must exist")
        write_log(filename=request_id, message=f"ERROR : Exactly one of SCORING_COMBINED or SCORING_RANDOM must exist")
        raise ValueError(f"Exactly one of SCORING_COMBINED or SCORING_RANDOM must exist")
    
    else:
        scoring_stage = next(iter(scoring_stage_set))
        
        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | {scoring_stage} set as scoring stage")

        missing_scoring_stages = scoring_group_set - stages_set

        all_stages = [s for s in all_stages if s not in missing_scoring_stages]

    all_stages_str = " >> ".join(all_stages)
    
    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | All stages validated")
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | {all_stages_str}")


    return all_stages, evaluation_stage, scoring_stage