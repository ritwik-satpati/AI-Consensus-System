# consensus_prompt_builder
MODULE_NAME = "CONSENSUS_PROMPT_BUILDER"

from functions.log_generator import write_log

# This function builds a combined prompt from all model responses
def build_consensus_prompt(original_prompt, structured_result, request_id):

    combined_prompt = f"Original Question::\n{original_prompt}\n\n"
    combined_prompt += "Model Responses::\n\n"

    for model, answer in structured_result.items():
        combined_prompt += f"{model}:\n{answer}\n\n"

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | PROCESS | Combined Prompt added | {model}")


    combined_prompt += (
        "Based on all the above responses, improve and refine the answer.\n"
        "If there are contradictions, resolve them logically and give only answer as output."
    )

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Combined Prompt created using {len(structured_result)} model responses")

    # print(combined_prompt)

    return combined_prompt