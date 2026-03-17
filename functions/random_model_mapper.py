# random_model_mapper.py
MODULE_NAME = "RANDOM_MODEL_MAPPER"

import random
from functions.log_generator import write_log
import json
import os


def generate_random_model_mapping(request_id, model_outputs, directory):
    """
    Generates random model mapping where:
    - Each model is evaluated by exactly one other model
    - No model evaluates its own output
    - Fair one-to-one mapping
    Returns => {evaluator_model : candidate_model}
    """

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | START | Random model mapping initiated")

    models = list(model_outputs.keys())

    if len(models) < 2:
        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Provided models = {len(models)} | Required models = 2")
        write_log(filename=request_id, message=f"ERROR : At least 2 models required for random model mapping")
        
        raise ValueError("At least 2 models required for cross evaluation.")

    shuffled = models[:]

    # Generate derangement (no self-matching)
    while True:
        random.shuffle(shuffled)
        if all(m1 != m2 for m1, m2 in zip(models, shuffled)):
            break
    
    # evaluator_model : candidate_model
    random_map = dict(zip(models, shuffled))

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Random model mapping generated")

     # Ensure structured folder exists
    os.makedirs(directory, exist_ok=True)

    # Generate timestamp-based filename
    filename = f"{directory}/{request_id}.json"

    # Save structured result
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(random_map, file, indent=4, ensure_ascii=False)

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Random model mapping saved | {filename}")

    return random_map