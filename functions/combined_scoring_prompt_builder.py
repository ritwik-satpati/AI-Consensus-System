# combined_scoring_prompt_builder.py

from functions.log_generator import write_log

def build_combined_scoring_prompt(original_prompt, combined_structured_result, request_id):

    prompt_text = f"""
You are an unbiased AI evaluator.

Original Question:
{original_prompt}

Below are responses from different AI agents:

"""

    for model, answer in combined_structured_result.items():
        prompt_text += f"\nAgent Name: {model}\nResponse:\n{answer}\n"

    prompt_text += """

Evaluate EACH agent independently using the following parameters:

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
    write_log(filename=request_id, message=f"COMBINED_SCORING_PROMPT_BUILDER | SUCCESS | Scoring Prompt created using {len(combined_structured_result.items())} model responses")
    
    return prompt_text