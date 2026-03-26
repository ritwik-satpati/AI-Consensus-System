# context_resolver.py
MODULE_NAME = "CONTEXT_RESOLVER"

from functions.log_generator import write_log


def get_structured_output_for_scoring(context):
    """
    Returns the structured output to be used for scoring.
    Priority:
    1. consensus_structured (if not None)
    2. fallback to initial_structured
    """

    structured_output = ""
    structured_output_name = ""

    if context.consensus_structured is not None:
        structured_output = context.consensus_structured
        structured_output_name = "consensus_structured"
    else:
        structured_output = context.initial_structured
        structured_output_name = "initial_structured"

    if structured_output is not None:
        # Updating log entry 
        write_log(filename=context.request_id, message=f"{MODULE_NAME} | SUCCESS | {structured_output_name} set as structured output")
        return structured_output
    else:
        # Updating log entry 
        write_log(filename=context.request_id, message=f"{MODULE_NAME} | FAILED | No stages found for structured_output")
        write_log(filename=context.request_id, message=f"ERROR : No structured output available from context")
        raise ValueError("No structured output available from context")
