# scoring_prompt_builder.py

from functions.log_generator import write_log

def build_scoring_prompt(original_prompt, model, answer, request_id):

    prompt_text = f"""
You are an unbiased AI evaluator.

Original Question:
{original_prompt}

Below is response from different AI agent(s):

"""

    prompt_text += f"\nAgent Name: {model}\nResponse:\n{answer}\n"

    prompt_text += """

Evaluate the agent independently using the following parameters:

1. Accuracy (1-10)
2. Clarity (1-10)
3. Completeness (1-10)
4. Conciseness (1-10)

Return STRICT JSON ONLY in this exact structure in a single line without JSON Structure:

{"agent_name": {"accuracy": number, "clarity": number, "completeness": number, "conciseness": number}}

Rules:
- Do NOT include explanations or comments.
- Output valid JSON only but one line without "\" or "\n"
- Scores must be integers between 1 and 10.
"""

    # Updating log entry 
    write_log(filename=request_id, message=f"SCORING_PROMPT_BUILDER | SUCCESS | Scoring Prompt created | {model}")
    
    return prompt_text