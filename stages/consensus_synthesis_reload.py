# consensus_synthesis_reload.py
MODULE_NAME = "CONSENSUS_SYNTHESIS_RELOAD"

from functions.stage_wrapper import stage_wrapper

base_module_name = MODULE_NAME.replace("_RELOAD", "")


@stage_wrapper(MODULE_NAME)
async def run_consensus_synthesis_reload(context, isPrint=False):
    """
    This function reloads previously saved consensus stage outputs (Replay / Debug Mode).

    - Loads raw consensus model responses from storage
    - Loads structured consensus results from storage
    - Stores structured output in context for downstream stages
    - Prints outputs for verification/debugging

    Useful for:
    - Debugging pipeline without re-running consensus stage
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

    # Load previously saved consensus round responses (useful for replay/debug)
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Consensus outputs
    consensus_outputs = (
        data.get("stages", {})
            .get(base_module_name, {})
            .get("consensus_outputs", {})
    )

    if isPrint:
        # Display final consensus round responses
        print(f"Consensus Output Result:\n{consensus_outputs}")

    # Consensus structured 
    consensus_structured = (
        data.get("stages", {})
            .get(base_module_name, {})
            .get("consensus_structured", {})
    )

    if isPrint:
        # Display final combined structured results
        print(f"Consensus Structured Result:\n{consensus_structured}")

    # Load current_satge_data in pipeline_context
    context.current_stage_data={
        "consensus_outputs": consensus_outputs,
        "consensus_structured": consensus_structured
    }

    # Load set_stage_output in pipeline_context
    context.set_stage_output(
        stage_name=base_module_name,
        outputs=consensus_outputs,
        structured=consensus_structured
    )

    # Load more components in pipeline_context
    context.consensus_structured = consensus_structured