# scoring_random_reload.py
MODULE_NAME = "SCORING_RANDOM_RELOAD"

from functions.stage_wrapper import stage_wrapper

base_module_name = MODULE_NAME.replace("_RELOAD", "")


@stage_wrapper(MODULE_NAME)
async def run_scoring_random_reload(context, isPrint=False):
    """
    This function reloads previously saved random scoring stage outputs (Replay / Debug Mode).

    - Loads raw scoring responses from storage
    - Loads structured scoring results from storage
    - Stores structured output in context for downstream stages
    - Prints outputs for verification/debugging

    Useful for:
    - Debugging pipeline without re-running scoring stage
    - Replay execution from saved state

    All logging, request_id handling, and execution tracking are managed by the stage wrapper.
    """

    # Import required modules for reload operation
    import json
    import os

    # Use existing request_id (must be set before pipeline execution)
    request_id = context.request_id

    # Validate request_id presence
    if not request_id:
        raise ValueError(f"{MODULE_NAME} | request_id is required for replay mode")

    # Define file paths
    path = f"outputs/{request_id}.json"

    # Validate file existence
    if not os.path.exists(path):
        raise FileNotFoundError(f"Output file not found: {path}")

    # Load previously saved raw scoring responses (useful for replay/debug)
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

   # Scoring outputs
    scoring_outputs = (
        data.get("stages", {})
            .get(base_module_name, {})
            .get("scoring_outputs", {})
        )

    if isPrint:
        # Display raw model output responses
        print(f"Scoring Outputs Result:\n{scoring_outputs}")

    # Scoring structured 
    scoring_structured = (
        data.get("stages", {})
            .get(base_module_name, {})
            .get("scoring_structured", {})
        )
    
    if isPrint:
        # Display final combined structured results
        print(f"Scoring Structured Result:\n{scoring_structured}")

    # Load current_satge_data in pipeline_context
    context.current_stage_data={
        # "scoring_outputs": scoring_outputs,
        # "scoring_structured": scoring_structured
    }

    # Load set_stage_output in pipeline_context
    context.set_stage_output(
        stage_name=base_module_name,
        outputs=scoring_outputs,
        structured=scoring_structured
    )

    # Load more components in pipeline_context
    context.scoring_structured = scoring_structured
