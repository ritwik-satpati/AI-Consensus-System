# winner_selector.py
MODULE_NAME = "WINNER_SELECTOR"

from functions.log_generator import write_log
from functions.json_exporter import export_json


def select_winner(final_results, request_id, directory=None):
    """
    Selects winner from ranked results.

    - winner  → first item (deterministic)
    - winners → all rank 1 models (handles ties)
    """

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | START | Selecting winner")

    if not final_results:
        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | No final results provided")
        write_log(filename=request_id, message=f"ERROR : No final results provided")
        return None

    # Primary winner (deterministic)
    winner = final_results[0]

    # All winners (tie case support) - all rank 1 models
    winners = [r for r in final_results if r.get("rank") == 1]

    data = {
        "winner": winner,
        "winners": winners 
    }

    # Save output
    export_json(
        request_id=request_id,
        directory=directory,
        data=data,
        data_label="Winner Details",
    )

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Winner selected | {data['winner']['model']} | {data['winner']['score']}")
    
    # Log tie case (only if multiple rank 1)
    if len(winners) > 1:
        models = [f"{w['model']}({w['score']})" for w in winners]

        # Updating log entry
        write_log(filename=request_id, message=(f"{MODULE_NAME} | SUCCESS | Multiple Winners selected | Rank 1 count: {len(winners)} | "+" | ".join(models)))

    return data