# consensus_synthesis.py
MODULE_NAME = "CONSENSUS_SYNTHESIS"

from functions.stage_wrapper import stage_wrapper


@stage_wrapper(MODULE_NAME)
async def run_consensus_synthesis(context):
    """
    This function performs consensus refinement (Round 2).

    - Builds consensus prompt using initial structured outputs
    - Executes all configured AI models with consensus prompt
    - Collects refined model outputs
    - Saves raw responses for audit/debug
    - Converts responses into structured format

    All logging, request_id handling, and execution tracking are managed by the stage wrapper.
    """

    # Import required modules for consensus stage execution
    from functions.consensus_prompt_builder import build_consensus_prompt
    from functions.ai_orchestrator import run_models
    from functions.response_formatter import format_structured_response

    # Build a consensus prompt using all Stage-1 model outputs
    consensus_prompt = build_consensus_prompt(
        original_prompt=context.base_prompt,
        structured_result=context.initial_structured,
        request_id=context.request_id
    )

    # Execute models again using the consensus prompt (Round 2 - Refinement)
    consensus_outputs = await run_models(
        prompt=consensus_prompt,
        system_prompt=context.system_prompt,
        models_data=context.model_configurations,
        request_id=context.request_id,
        stage=MODULE_NAME,
        # directory="outputs/consensus_outputs",
    )

    # Convert consensus responses into structured format
    consensus_structured = format_structured_response(
        request_id=context.request_id,
        data=consensus_outputs,
        stage=MODULE_NAME,
        # directory="outputs/consensus_structured",
    )

    # Load current_satge_data in pipeline_context
    context.current_stage_data={
        "consensus_outputs": consensus_outputs,
        "consensus_structured": consensus_structured
    }

    # Load set_stage_output in pipeline_context
    context.set_stage_output(
        stage_name=MODULE_NAME,
        outputs=consensus_outputs,
        structured=consensus_structured
    )

    # Load more components in pipeline_context
    context.consensus_structured = consensus_structured