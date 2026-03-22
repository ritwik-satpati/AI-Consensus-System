# test.py

MODULE_NAME = "TEST"

from dotenv import load_dotenv
from functions.log_generator import write_log
from pipeline_context import PipelineContext

# Load environment variables from .env file
load_dotenv()


def test(request_id_override=None):
    """
    This function is used for internal testing / replay / debugging.

    - Allows manual request_id override
    - Can simulate pipeline stages
    - Useful for debugging specific scenarios
    """

    # Initialize context
    context = PipelineContext()

    # Use override request_id if provided
    context.request_id = request_id_override or "XXXX_XXXXXX_XXXXXX"

    # Hardcoded prompts (for testing)
    context.base_prompt = "Explain API in simple words within 100 words"
    context.system_prompt = "You are a helpful assistant."

    # Updating log entry
    write_log(
        filename=context.request_id, message=f"{MODULE_NAME} | START | Used for replay/debug")

    print("This is for internal testing!")

    # =========================
    # Testing code - Start
    # =========================

    pass

    # =========================
    # Testing code - End
    # =========================

    # Updating log entry
    write_log(filename=context.request_id, message=f"{MODULE_NAME} | END | Used for replay/debug")

    return True