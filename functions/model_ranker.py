# model_ranker.py
MODULE_NAME = "MODEL_RANKER"

from functions.log_generator import write_log
from functions.json_exporter import export_json


def rank_models(context, final_scores, directory=None):
    """
    Returns ranking list like:
    [{rank: 1, model: 'gpt', score: 0.92}, ...]
    """

    if not final_scores:
        # Updating log entry 
        write_log(filename=context.request_id, message=f"{MODULE_NAME} | FAILED | No scores provided")
        write_log(filename=context.request_id, message=f"ERROR : No scores provided during rankking model.")
        return []

    # Sort models by score (descending)
    sorted_models = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)

    rankings = []
    prev_score = None

    for idx, (model, score) in enumerate(sorted_models):

        if prev_score is not None and score == prev_score:
            rank = rankings[-1]["rank"]
        else:
            rank = idx + 1

        rankings.append({
            "rank": rank,
            "model": model,
            "score": score,
        })

        prev_score = score

        # Updating log entry 
        write_log(filename=context.request_id, message=f"{MODULE_NAME} | SUCCESS | Added Rank {rank} | {model} | {score}")

        prev_score = score

    # Updating log entry 
    write_log(filename=context.request_id, message=f"{MODULE_NAME} | SUCCESS | Models Ranked | Total models ranked {rank}")

    # Save the output using export_json
    export_json(
        request_id=context.request_id,
        directory=directory,
        data=rankings,
        data_label="Model Rankings",
    )

    return rankings