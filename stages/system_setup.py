# system_setup.py
MODULE_NAME = "SYSTEM_SETUP"

from functions.stage_wrapper import stage_wrapper


@stage_wrapper(MODULE_NAME)
async def run_system_setup(context):
    """
    This function performs initial pipeline setup.

    - Initializes request_id (test or generated)
    - Initializes execution timing
    - Captures start timestamp
    - Loads base prompt and system prompt
    - Loads configured AI model settings

    Stage execution tracking (logging, timing) is handled by the stage wrapper.
    """

    import time
    from functions.time_utils import get_current_time
    from hardcodes.prompt_manager import get_prompt
    from hardcodes.system_prompt_manager import get_system_prompt
    from hardcodes.model_manager import get_models
    from functions.request_id_generator import generate_request_id
    from hardcodes.test_request_id_manager import get_test_request_id
    from functions.model_utils import get_safe_models

     # Start total execution timer
    start_perf_counter = time.perf_counter()

    # Readable start timestamp
    start_timestamp = get_current_time()

    # Check if test request_id is provided (Replay Mode)
    test_request_id = get_test_request_id()

    if test_request_id:
        request_id = test_request_id

    # Otherwise generate a new request_id (Normal Mode)
    elif not getattr(context, "request_id", None):

        # Ensure request_id exists
        initial_log_messages = ["AI_CONSENSUS_SYSTEM | START | V3 - Version 1.2.0"]

        # Initial log messages for pipeline start
        request_id = generate_request_id(pre_log_messages=initial_log_messages)

    # Base prompt
    base_prompt = get_prompt(request_id=request_id)

    # System prompt
    system_prompt = get_system_prompt(request_id=request_id)

    # Model configurations
    model_configurations = get_models(request_id=request_id)

    # Masking API key for models
    safe_models = get_safe_models(request_id=request_id, models=model_configurations)

    # Load current_satge_data in pipeline_context
    context.current_stage_data={
        "request_id": request_id,
        "start_timestamp": start_timestamp,
        "base_prompt": base_prompt,
        "system_prompt": system_prompt,
        "models_loaded": len(model_configurations),
        "model_configurations": safe_models,
    }

    # Load more components in pipeline_context
    context.start_perf_counter = start_perf_counter
    context.start_timestamp = start_timestamp
    context.request_id = request_id
    context.base_prompt = base_prompt
    context.system_prompt = system_prompt
    context.model_configurations = model_configurations