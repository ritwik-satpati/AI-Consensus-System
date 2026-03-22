# score_aggregation.py.py
MODULE_NAME = "SCORE_AGGREGATION"

from functions.stage_wrapper import stage_wrapper


@stage_wrapper(MODULE_NAME)
async def run_score_aggregation(context):
    """
    This function performs score aggregation and winner selection.

    - Parses scoring outputs into structured score matrix
    - Aggregates scores across evaluators
    - Calculates weighted final scores
    - Selects the winning model based on highest score
    - Saves intermediate and final scoring data for audit

    All logging, request_id handling, and execution tracking
    are managed by the stage wrapper.
    """

    # Import required modules for aggregation stage execution
    from functions.score_parser import parse_scoring_outputs
    from functions.score_aggregator import aggregate_model_scores
    from functions.final_score_calculator import calculate_weighted_score

    # Parse stringified JSON score outputs into proper Python dictionary
    parsed_scores = parse_scoring_outputs(
        raw_scores=context.scoring_structured,
        request_id=context.request_id,
        # directory="outputs/raw_scores"
    )

    # Aggregate scores across evaluators (optionally remove self-scoring bias)
    aggregated_scores = aggregate_model_scores(
        parsed_scores=parsed_scores,
        request_id=context.request_id,
        remove_self_bias=False,
        # remove_self_bias=True,
        # directory="outputs/aggregated_scores"
    )

    # Calculate weighted final score per model
    weighted_scores = calculate_weighted_score(
        agent_scores=aggregated_scores,
        request_id=context.request_id,
        # directory="outputs/weighted_scores"
    )

    # Load current_satge_data in pipeline_context
    context.current_stage_data={
        "parsed_scores": parsed_scores,
        "aggregated_scores": aggregated_scores,
        "weighted_scores": weighted_scores,
    }

    # Load more components in pipeline_context
    context.weighted_scores = weighted_scores