# response_formatter.py
MODULE_NAME = "RESPONSE_FORMATTER"

# Import modules
from functions.log_generator import write_log
from functions.json_exporter import export_json


def format_structured_response(request_id, data, stage, directory=None):
    """
    This function converts raw AI outputs into structured model-output format
    """
    
    # Create dictionary: { model_name : model_output }
    result = {item["model"]: item["output"] for item in data}
    
    # Save the output using export_json
    export_json(
        request_id=request_id,
        directory=directory,
        data=result,
        data_label=f"{"Structured Outputs for {stage}"}",
    )

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Structured outputs created | For stage {stage}")

    return result