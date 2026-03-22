# combined_scoring_prompt_builder.py
MODULE_NAME = "COMBINED_SCORING_PROMPT_BUILDER"

from functions.log_generator import write_log


def build_combined_scoring_prompt(original_prompt, combined_structured_result, request_id):
    """
    This function used to create propmt using combined_structured_result at once for multiple models.
    """
    
    first_model = list(combined_structured_result.keys())[0]

    prompt_text = f"""
You are an unbiased AI evaluator.

Original Question:
{original_prompt}

Below are responses from different AI agents:
"""

    for model, answer in combined_structured_result.items():
        prompt_text += f"\nAgent Name: {model}\nResponse:\n{answer}\n"

    prompt_text += """

Evaluate EACH agent independently using the following criteria (score each from 1 to 10):
1. Accuracy – Correctness of the information.
2. Clarity – How easy the response is to understand.
3. Completeness – How well the response answers the question.
4. Conciseness – Whether the response is brief and avoids unnecessary information.

Instructions::
- Evaluate each agent independently.
- Scores must be integers between 1 and 10.
- Use the EXACT agent names provided after "Agent Name: " as JSON keys.
- Return ONLY valid JSON.
- Do NOT include explanations, reasoning, or text outside the JSON.
- Output must be a single-line JSON object.

Correct Output Example:
{{"{first_model}": {{"accuracy": 9, "clarity": 9, "completeness": 8, "conciseness": 9}}}}

Wrong Output Examples:
{{"agent_name": {{"{first_model}": {{"accuracy": 9, "clarity": 10, "completeness": 9, "conciseness": 9}}}}}}
{{"agent_name": {{"accuracy": 10, "clarity": 10, "completeness": 9, "conciseness": 9}}}}
"""

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Scoring Prompt created using {len(combined_structured_result.items())} model responses")

    return prompt_text