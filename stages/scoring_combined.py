# scoring_combined.py
MODULE_NAME = "SCORING_COMBINED"

from functions.stage_wrapper import stage_wrapper


@stage_wrapper(MODULE_NAME)
async def run_scoring_combined(context):
    """
    This function performs combined scoring (Round 3 - Evaluation).

    - Builds scoring prompt using consensus structured outputs
    - Executes all configured AI models for evaluation
    - Collects scoring outputs
    - Saves raw scoring responses for audit/debug
    - Converts responses into structured format

    All logging, request_id handling, and execution tracking are managed by the stage wrapper.
    """

    # Import required modules for scoring stage execution
    from functions.combined_scoring_prompt_builder import build_combined_scoring_prompt
    from functions.ai_orchestrator import run_models
    from functions.response_formatter import format_structured_response
    from functions.context_resolver import get_structured_output_for_scoring

    # Select structured_output for scoring prompt
    structured_output = get_structured_output_for_scoring(
        context=context
    )

    # Build scoring prompt to evaluate consensus outputs
    scoring_prompt = build_combined_scoring_prompt(
        original_prompt=context.base_prompt,
        combined_structured_result=structured_output,
        request_id=context.request_id
    )

    # Execute scoring round (Round 3 - Evaluation)
    scoring_outputs = await run_models(
        prompt=scoring_prompt,
        system_prompt=context.system_prompt,
        models_data=context.model_configurations,
        request_id=context.request_id,
        stage=MODULE_NAME,
        # directory="outputs/scoring_outputs",
    )

    # Convert scoring outputs into structured format (model → JSON score string)
    scoring_structured = format_structured_response(
        request_id=context.request_id,
        data=scoring_outputs,
        stage=MODULE_NAME,
        # directory="outputs/scoring_structured",
    )

    # Load current_satge_data in pipeline_context
    context.current_stage_data={
        "scoring_outputs": scoring_outputs,
        "scoring_structured": scoring_structured
    }

    # Load set_stage_output in pipeline_context
    context.set_stage_output(
        stage_name=MODULE_NAME,
        outputs=scoring_outputs,
        structured=scoring_structured
    )

    # Load more components in pipeline_context
    context.scoring_structured = scoring_structured