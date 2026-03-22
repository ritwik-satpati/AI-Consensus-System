# scoring_random.py
MODULE_NAME = "SCORING_RANDOM"

from functions.stage_wrapper import stage_wrapper


@stage_wrapper(MODULE_NAME)
async def run_scoring_random(context):
    """
    This function performs scoring using random model mapping (Round 3 - Evaluation).

    - Generates random mapping of model outputs
    - Builds model-specific scoring prompts
    - Executes scoring with custom prompts
    - Saves raw scoring responses for audit/debug
    - Converts responses into structured format

    All logging, request_id handling, and execution tracking are managed by the stage wrapper.
    """

    # Import required modules for random scoring stage execution
    from functions.random_model_mapper import generate_random_model_mapping
    from functions.scoring_prompt_orchestrator import build_scoring_prompt_orchestrator
    from functions.ai_orchestrator import run_models
    from functions.response_formatter import format_structured_response

    # Generate random model mapping
    random_model_map = generate_random_model_mapping(
        request_id=context.request_id,
        model_outputs=context.consensus_structured,
        # directory="outputs/model_mapping"
    )

    # Build scoring prompt for mapped model outputs
    prompts_with_model = build_scoring_prompt_orchestrator(
        request_id=context.request_id,
        original_prompt=context.base_prompt,
        random_map=random_model_map,
        model_outputs=context.consensus_structured,
    )

    # Execute scoring round (Round 3 - Evaluation) with custom prompts
    scoring_outputs = await run_models(
        prompts_with_model=prompts_with_model,
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
        "random_model_map": random_model_map,
        "prompts_with_model": prompts_with_model,
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