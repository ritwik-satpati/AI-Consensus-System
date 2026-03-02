# winner_selector.py

from functions.log_generator import write_log

# This function selects the highest scoring model
# and returns its score and output
def select_winner(final_scores, combined_model_outputs, request_id):

    if not final_scores:
        return None

    # Step 1: Pick model with highest score
    best_model = max(final_scores, key=final_scores.get)
    best_score = final_scores[best_model]

    # Step 2: Extract that model's output
    best_output = next(
        (item["output"] for item in combined_model_outputs if item["model"] == best_model),
        None
    )

    data = {
        "model": best_model,
        "score": best_score,
        "output": best_output
    }

    # Updating log entry 
    write_log(filename=request_id, message=f"WINNER_SELECTOR | SUCCESS | Winner selected | {best_model} | {best_score}")

    return data