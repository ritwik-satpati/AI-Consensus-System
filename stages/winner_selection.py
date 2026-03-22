# winner_selectionn.py
MODULE_NAME = "WINNER_SELECTION"

from functions.stage_wrapper import stage_wrapper


@stage_wrapper(MODULE_NAME)
async def run_winner_selection(context):
    """
    This function select the winner and its details and logging.

    - Captures pipeline end timestamp
    - Calculates total execution time
    - Saves winning model output with metadata

    All logging, request_id handling, and execution tracking are managed by the stage wrapper.
    """

    # Import required modules for reporting stage execution
    import time
    from functions.model_ranker import rank_models
    from functions.result_formatter import format_ranked_results
    from functions.time_utils import get_current_time
    from functions.log_generator import write_log
    from functions.winner_selector import select_winner
    from functions.winner_logger import save_more_details

    # Winning output from
    winner_output_stage = "CONSENSUS_SYNTHESIS"

    model_rankings = rank_models(
        context=context, 
        final_scores=context.weighted_scores
        # directory="outputs/model_rankings"
    )    

    final_results = format_ranked_results(
        context=context,
        rankings=model_rankings,
        model_outputs=context.stages_output.get(winner_output_stage, {}).get("outputs", [])
        # directory="outputs/final_results"
    )

    # Select winning model based on highest weighted score
    winner_details = select_winner(
        final_results=final_results,
        request_id=context.request_id,
        # directory="outputs/winner_details"
    )

    # Stop performance timer
    end_perf_counter = time.perf_counter()

    # Readable end timestamp
    end_timestamp = get_current_time()

    # Updating log entry 
    write_log(filename=context.request_id, message=f"{MODULE_NAME} | SUCCESS | End Timestamp captured", current_time=end_timestamp)

    # Calculate total pipeline execution time (in seconds)
    execution_time = round(end_perf_counter - context.start_perf_counter, 4)

    # Updating log entry 
    write_log(filename=context.request_id, message=f"{MODULE_NAME} | SUCCESS | Total pipeline execution time {execution_time} seconds")

    # Save more details like metadata and timing info
    more_details = save_more_details(
        request_id=context.request_id,
        prompt=context.base_prompt,
        start_time=context.start_timestamp,
        end_time=end_timestamp,
        execution_time=execution_time,
        winner_details=winner_details
        # directory="outputs/more_details"
    )

    # Load set_stage_output in pipeline_context
    context.current_stage_data={
        "winner_output_stage": winner_output_stage,
        "model_rankings": model_rankings,
        "final_results": final_results,
        "winner_details": winner_details,
        "more_details": more_details,
    }

    # Load more components in pipeline_context
    context.winner_details = winner_details
    context.end_timestamp = end_timestamp
    context.execution_time = execution_time