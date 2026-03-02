# score_parser.py

# Import JSON module for parsing stringified JSON
import json
from functions.log_generator import write_log

# This function converts AI scoring outputs into usable Python dictionaries
def parse_scoring_outputs(raw_scores, request_id):

    # Updating log entry    
    write_log(filename=request_id, message="SCORE_PARSER | START | Parsing scoring outputs initiated")

    # Dictionary to store successfully parsed evaluator outputs
    parsed_results = {}

    # Loop through each evaluator agent and its raw score output
    for evaluator_agent, score_data in raw_scores.items():

        try:
            # Case 1: If evaluator already returned a dictionary → accept directly
            if isinstance(score_data, dict):

                parsed_results[evaluator_agent] = score_data

                # Updating log entry
                write_log( filename=request_id, message=f"SCORE_PARSER | SUCCESS | Dictionary accepted directly | {evaluator_agent}")

                continue

            # Case 2: If evaluator returned string → attempt JSON parsing
            if isinstance(score_data, str):

                try:
                    # Attempt normal JSON parsing
                    parsed_json = json.loads(score_data)

                    parsed_results[evaluator_agent] = parsed_json

                    # Updating log entry
                    write_log( filename=request_id, message=f"SCORE_PARSER | SUCCESS | JSON string parsed | {evaluator_agent}")

                    continue

                except json.JSONDecodeError:
                    # Fallback Case: Multiple JSON blocks separated by newline
                    merged_result = {}

                    # Split by newline and remove empty blocks
                    blocks = [b.strip() for b in score_data.split("\n") if b.strip()]

                    # Parse and merge each JSON block
                    for block in blocks:
                        block_json = json.loads(block)
                        merged_result.update(block_json)

                    parsed_results[evaluator_agent] = merged_result

                    # Updating log entry
                    write_log( filename=request_id, message=f"SCORE_PARSER | SUCCESS | Multi-JSON merged | {evaluator_agent}")

                    continue

            # Case 3: Unsupported data type
            # Updating log entry
            write_log( filename=request_id, message=f"SCORE_PARSER | FAILED | Unsupported data format | {evaluator_agent}")
            write_log( filename=request_id, message=f"ERROR : Unsupported data format = {evaluator_agent}")

        except Exception as e:
            # Catch unexpected errors (safety net for production stability)

            # Updating log entry
            write_log( filename=request_id, message=f"SCORE_PARSER | FAILED | {evaluator_agent}")
            write_log( filename=request_id, message=f"ERROR : {str(e)}")

    # Updating log entry
    write_log(filename=request_id, message=f"SCORE_PARSER | SUCCESS | Parsed {len(parsed_results)} evaluator results")

    return parsed_results