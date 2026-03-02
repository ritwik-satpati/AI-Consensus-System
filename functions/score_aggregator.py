# score_aggregator.py

from functions.log_generator import write_log

def aggregate_model_scores(parsed_scores, request_id, remove_self_bias=True):

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
        write_log(filename=request_id, message=f"SCORE_AGGREGATOR | PROCESS | Averaged scores computed | {agent}")

    # Updating log entry 
    write_log(filename=request_id, message=f"SCORE_AGGREGATOR | SUCCESS | Aggregated scores generated for {len(averaged)} agents")
    write_log(filename=request_id, message=f"SCORE_AGGREGATOR | SUCCESS | Self-bias removed = {remove_self_bias}")

    return averaged