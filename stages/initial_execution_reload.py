# initial_execution_reload.py
MODULE_NAME = "INITIAL_EXECUTION_RELOAD"

from functions.stage_wrapper import stage_wrapper

base_module_name = MODULE_NAME.replace("_RELOAD", "")


@stage_wrapper(MODULE_NAME)
async def run_initial_execution_reload(context, isPrint=False):
    """
    This function reloads previously saved initial stage outputs (Replay / Debug Mode).

    - Loads raw model responses from storage
    - Loads structured responses from storage
    - Stores structured output in context for downstream stages
    - Prints outputs for verification/debugging

    Useful for:
    - Debugging pipeline without re-running models
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

    # Load previously saved raw model responses (useful for replay/debug)
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Initial outputs
    initial_outputs = (
        data.get("stages", {})
            .get(base_module_name, {})
            .get("initial_outputs", {})
        )

    if isPrint:
        # Display raw model output responses
        print(f"Initial Outputs Result:\n{initial_outputs}")

    # Initial structured 
    initial_structured = (
        data.get("stages", {})
            .get(base_module_name, {})
            .get("initial_structured", {})
        )

    if isPrint:
        # Display final combined structured results
        print(f"Initial Structured Result:\n{initial_structured}")


    # Load current_satge_data in pipeline_context
    context.current_stage_data={
        # "initial_outputs": initial_outputs,
        # "initial_structured": initial_structured
    }
    
    # Load set_stage_output in pipeline_context
    context.set_stage_output(
        stage_name=base_module_name,
        outputs=initial_outputs,
        structured=initial_structured
    )
    
    # Load initial_structured
    context.initial_structured = initial_structured