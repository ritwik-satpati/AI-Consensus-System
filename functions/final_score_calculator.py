# final_score_calculator.py
MODULE_NAME = "FINAL_SCORE_CALCULATOR"

from functions.log_generator import write_log

def calculate_weighted_score(agent_scores, request_id):

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | START | Calculating weighted scores")

    weights = {
        "accuracy": 0.4,
        "clarity": 0.2,
        "completeness": 0.3,
        "conciseness": 0.1
    }

    final = {}

    for agent, metrics in agent_scores.items():

        score = sum(metrics[m] * weights[m] for m in weights)

        final[agent] = round(score, 2)

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | PROCESS | Weighted score computed for {agent}")
    
    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Weighted scores calculated for {len(final)} agents")
    

    return final