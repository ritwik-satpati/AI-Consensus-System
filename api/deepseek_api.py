# deepseek_api.py

from openai import OpenAI
from dotenv import load_dotenv
from models.response_data import get_response_data
from functions.log_generator import write_log


# Load environment variables
load_dotenv()


# This function sends a prompt to DeepSeek and returns structured response data
def call_deepseek(prompt, model, key, request_id):

    # DeepSeek uses OpenAI-compatible API format
    client = OpenAI(
        api_key=key,
        base_url="https://api.deepseek.com/"   # DeepSeek base URL
    )

    response = None  # Predefine response for safer exception handling

    try:
        # Updating log entry
        write_log(filename=request_id, message=f"DEEPSEEK_API | START | Request initiated | {model}")

        # API Call
        response = client.chat.completions.create(
            model=model,   # Example: deepseek-chat / deepseek-coder
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Updating log entry
        write_log(filename=request_id, message=(f"DEEPSEEK_API | SUCCESS | Response received | {model} | Prompt Tokens = {response.usage.prompt_tokens} | Completion Tokens = {response.usage.completion_tokens}"))

        # Return Success Data
        return get_response_data(
            model_id=model,
            output=response.choices[0].message.content,
            p_tokens=response.usage.prompt_tokens,
            c_tokens=response.usage.completion_tokens,
            status="success"
        )

    except Exception as e:

        # Default token values
        p_tokens = 0
        c_tokens = 0

        # If response exists and usage is available
        if response and hasattr(response, "usage") and response.usage:
            p_tokens = response.usage.prompt_tokens or 0
            c_tokens = response.usage.completion_tokens or 0

        # Updating log entry
        write_log(filename=request_id, message=(f"DEEPSEEK_API | FAILED | Error during API call | {model} | Prompt Tokens = {p_tokens} | Completion Tokens = {c_tokens}"))
        write_log(filename=request_id, message=f"ERROR : {str(e)}")
        print(e)

        # Return Error Data
        return get_response_data(
            model_id=model,
            status="error",
            error=str(e),
            p_tokens=p_tokens,
            c_tokens=c_tokens
        )