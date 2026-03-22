# initial_execution.py
MODULE_NAME = "INITIAL_EXECUTION"

from functions.stage_wrapper import stage_wrapper


@stage_wrapper(MODULE_NAME)
async def run_initial_execution(context):
    """
    This function performs initial model execution (Round 1 - Generation).

    - Executes all configured AI models using base prompt
    - Collects raw model outputs
    - Saves raw responses for audit/debug
    - Converts responses into structured format

    All logging, request_id handling, and execution tracking are managed by the stage wrapper.
    """

    # Import required modules for initial stage execution
    from functions.ai_orchestrator import run_models
    from functions.response_formatter import format_structured_response

    # Run all configured models with the base prompt (Round 1 - Generation)
    initial_outputs = await run_models(
        prompt=context.base_prompt,
        system_prompt=context.system_prompt,
        models_data=context.model_configurations,
        request_id=context.request_id,
        stage=MODULE_NAME,
        # directory="outputs/initial_outputs",
    )

    # Convert raw responses into structured format: { model_name : output }
    initial_structured = format_structured_response(
        request_id=context.request_id,
        data=initial_outputs,
        stage=MODULE_NAME,
        # directory="outputs/initial_structured",
    )

    # Load current_satge_data in pipeline_context
    context.current_stage_data={
        "initial_outputs": initial_outputs,
        "initial_structured": initial_structured
    }
    
    # Load set_stage_output in pipeline_context
    context.set_stage_output(
        stage_name=MODULE_NAME,
        outputs=initial_outputs,
        structured=initial_structured
    )

    # Load more components in pipeline_context
    context.initial_structured = initial_structured