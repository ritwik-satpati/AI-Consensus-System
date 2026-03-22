# grok_api.py
MODULE_NAME = "GROK_API"

import os
from xai_sdk import Client
from xai_sdk.chat import user, system
from dotenv import load_dotenv
from models.response_data import get_response_data
from functions.log_generator import write_log


# Load environment variables
load_dotenv()


async def call_grok(prompt, model, key, system_prompt, request_id):
    """
    This function sends a prompt to Grok (xAI) and returns structured response data
    """
    
    client = Client(api_key=key)

    response = None

    try:

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | START | Request initiated | {model}")

        # Create chat session
        chat = client.chat.create(model=model)

        chat.append(system(system_prompt))
        chat.append(user(prompt))

        # Generate response
        response = chat.sample()

        output_text = response.content

        # xAI SDK currently does not expose token usage reliably
        p_tokens = getattr(response, "prompt_tokens", 0)
        c_tokens = getattr(response, "completion_tokens", 0)

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Response received | {model} | Prompt Tokens = {p_tokens} | Completion Tokens = {c_tokens}")

        # Return Success Data
        return get_response_data(
            model_id=model,
            provider_name="xai",
            input=prompt,
            output=output_text,
            p_tokens=p_tokens,
            c_tokens=c_tokens,
            status="success"
        )

    except Exception as e:

        p_tokens = 0
        c_tokens = 0

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Error during API call | {model} | Prompt Tokens = {p_tokens} | Completion Tokens = {c_tokens}")
        write_log(filename=request_id, message=f"ERROR : {str(e)}")

        # Return Error Data
        return get_response_data(
            model_id=model,
            provider_name="xai",
            input=prompt,
            status="error",
            error=str(e),
            p_tokens=p_tokens,
            c_tokens=c_tokens
        )