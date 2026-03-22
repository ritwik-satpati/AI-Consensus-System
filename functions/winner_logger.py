# score_logger.py
MODULE_NAME = "WINNER_LOGGER"

# Import required modules
from functions.log_generator import write_log
from functions.json_exporter import export_json


def save_more_details(request_id, prompt, start_time, end_time, execution_time, winner_details, directory=None):
    """
    This function saves more details related to winning into a JSON file
    """

    winners = winner_details.get("winners") or []
    winner = winner_details.get("winner") or {}

    # Structure the score output
    data = {
        "request_id": request_id,
        "prompt": prompt,
        "start_time": start_time,
        "end_time": end_time,
        "execution_time": execution_time,
        "winner_model": winner.get("model"),
        "winners_count": len(winners),
        "top_models": [w.get("model") for w in winners],
    }

    # Save the output using export_json
    export_json(
        request_id=request_id,
        directory=directory,
        data=data,
        data_label="More Details",
    )

    return data