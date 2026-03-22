# result_formatter.py
MODULE_NAME = "RESULT_FORMATTER"

from functions.log_generator import write_log
from functions.json_exporter import export_json


def format_ranked_results(context, rankings, model_outputs, directory=None):
    """
    Enrich rankings with provider, output, and score details.

    Returns:
    [
        {
            "rank": 1,
            "model": "gpt",
            "provider": "openai",
            "score": 0.92,
            "output": "..."
        }
    ]
    """

    if not rankings:
        # Updating log entry 
        write_log(filename=context.request_id, message=f"{MODULE_NAME} | FAILED | No rankings provided")
        write_log(filename=context.request_id, message=f"ERROR : No ranking provided during formatting results.")
        return []

    # Convert model_outputs list → dictionary for O(1) lookup
    output_map = {
        item["model"]: item
        for item in model_outputs
    }

    formatted_results = []

    for item in rankings:
        model = item["model"]

        output_data = output_map.get(model, {})

        formatted_item = {
            "rank": item["rank"],
            "model": model,
            "provider": output_data.get("provider"),
            "score": item["score"],
            "output": output_data.get("output"),
        }

        formatted_results.append(formatted_item)

        # Updating log entry 
        write_log(filename=context.request_id, message=f"{MODULE_NAME} | SUCCESS | Formatted Result added for Rank {item['rank']} | {model}")

    # Updating log entry 
    write_log(filename=context.request_id, message=f"{MODULE_NAME} | SUCCESS | Result formatted")

    # Save the output using export_json
    export_json(
        request_id=context.request_id,
        directory=directory,
        data=rankings,
        data_label="Final Results",
    )

    return formatted_results