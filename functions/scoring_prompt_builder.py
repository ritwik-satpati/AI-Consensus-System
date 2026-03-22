# scoring_prompt_builder.py
MODULE_NAME = "SCORING_PROMPT_BUILDER"

from functions.log_generator import write_log


def build_scoring_prompt(original_prompt, model, answer, request_id):
    """
    This function used to create propmt for single model for random scoring.
    """

    prompt_text = f"""
You are an unbiased AI evaluator.

Original Question:
{original_prompt}

Below is response from different AI agent(s):

"""

    prompt_text += f"\nAgent Name: {model}\nResponse:\n{answer}\n"

    prompt_text += """

Evaluate agent independently using the following criteria (score each from 1 to 10):
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
{{"{model}": {{"accuracy": 9, "clarity": 9, "completeness": 8, "conciseness": 9}}}}

Wrong Output Examples:
{{"agent_name": {{"{model}": {{"accuracy": 9, "clarity": 10, "completeness": 9, "conciseness": 9}}}}}}
{{"agent_name": {{"accuracy": 10, "clarity": 10, "completeness": 9, "conciseness": 9}}}}
"""

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Scoring Prompt created | {model}")
    
    return prompt_text