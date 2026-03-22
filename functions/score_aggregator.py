# score_aggregator.py
MODULE_NAME = "SCORE_AGGREGATOR"

from functions.log_generator import write_log
from functions.json_exporter import export_json


def aggregate_model_scores(parsed_scores, request_id, remove_self_bias=False, directory=False):
    """
    This function average all the aggregate scores from all models (optionally remove self-scoring bias) 
    """
    
    collected = {}

    for evaluator, evaluations in parsed_scores.items():

        for target, metrics in evaluations.items():

            # Remove self-scoring if enabled
            if remove_self_bias and evaluator == target:
                continue

            if target not in collected:
                collected[target] = {
                    "accuracy": [],
                    "clarity": [],
                    "completeness": [],
                    "conciseness": []
                }

            for metric, value in metrics.items():
                collected[target][metric].append(value)

    # Compute averages
    averaged = {}

    for agent, metrics in collected.items():

        averaged[agent] = {
            metric: round(sum(values) / len(values), 2)
            for metric, values in metrics.items()
        }

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | PROCESS | Averaged scores computed | {agent}")

    # Save the output using export_json
    export_json(
        request_id=request_id,
        directory=directory,
        data=averaged,
        data_label="Aggregated Scores",
    )

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Aggregated scores generated for {len(averaged)} agents")
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Self-bias removed = {remove_self_bias}")

    return averaged