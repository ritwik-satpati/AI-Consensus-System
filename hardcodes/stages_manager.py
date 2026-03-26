# stages_manager.py
MODULE_NAME = "MODEL_MANAGER"

# Import
from functions.log_generator import write_log


def get_stages(request_id):
    """ 
    This function manages Stages selection
    Optional Step => "CONSENSUS_SYNTHESIS"
    Choose one => "SCORING_COMBINED" / "SCORING_RANDOM_RELOAD"
    Rest all (not " _)
    """

    """
    Combinations ::
    SYSTEM_SETUP >> INITIAL_EXECUTION >> CONSENSUS_SYNTHESIS >> SCORING_COMBINED >> SCORE_AGGREGATION >> WINNER_SELECTION >> REPORT_GENERATION
    SYSTEM_SETUP >> INITIAL_EXECUTION >> CONSENSUS_SYNTHESIS >> SCORING_RANDOM >> SCORE_AGGREGATION >> WINNER_SELECTION >> REPORT_GENERATION
    SYSTEM_SETUP >> INITIAL_EXECUTION >> SCORING_COMBINED >> SCORE_AGGREGATION >> WINNER_SELECTION >> REPORT_GENERATION
    SYSTEM_SETUP >> INITIAL_EXECUTION >> SCORING_RANDOM >> SCORE_AGGREGATION >> WINNER_SELECTION >> REPORT_GENERATION
    """

    stages = [
        "SYSTEM_SETUP",
        "INITIAL_EXECUTION",
        # # "INITIAL_EXECUTION_RELOAD",
        "CONSENSUS_SYNTHESIS",
        # # "CONSENSUS_SYNTHESIS_RELOAD",
        "SCORING_COMBINED",
        # # "SCORING_COMBINED_RELOAD",
        # "SCORING_RANDOM",
        # # "SCORING_RANDOM_RELOAD",
        "SCORE_AGGREGATION",
        "WINNER_SELECTION",
        "REPORT_GENERATION"
    ]

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Stages configurations loaded")

    # Return structured Stages data
    return stages