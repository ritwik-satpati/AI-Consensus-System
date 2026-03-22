# claude_api.py
MODULE_NAME = "CLAUDE_API"

# from anthropic import Anthropic
from anthropic import AsyncAnthropic
from dotenv import load_dotenv
from models.response_data import get_response_data
from functions.log_generator import write_log
import httpx


# Load environment variables
load_dotenv()


async def call_claude(prompt, model, key, system_prompt, request_id):
    """
    This function sends a prompt to Claude and returns the response
    """
    
    # Create Anthropic client using the API key from .env
    client = AsyncAnthropic(
        api_key=key,
        http_client=httpx.AsyncClient(verify=False)
    )

    try:
        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | START | Request initiated | {model}")

        # API Call
        response = await client.messages.create(
            model=model,
            max_tokens=8096,
            system=system_prompt,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # print(response)

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Response received | {model} | Prompt Tokens = {response.usage.input_tokens} | Completion Tokens = {response.usage.output_tokens}")

        # Return Success Data
        return get_response_data(
            model_id=model,
            provider_name="anthropic",
            input=prompt,
            output=response.content[0].text,
            p_tokens=response.usage.input_tokens,
            c_tokens=response.usage.output_tokens,
            status="success"
        )

    except Exception as e:
        # Fallback token extraction if the API failed midway
        p_tokens = 0
        c_tokens = 0
        if 'response' in locals() and hasattr(response, 'usage') and response.usage:
            p_tokens = response.usage.input_tokens or 0
            c_tokens = response.usage.output_tokens or 0

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Error during API call | {model} | Prompt Tokens = {p_tokens} | Completion Tokens = {c_tokens}")
        write_log(filename=request_id, message=f"ERROR : {str(e)}'")

        # Return Error Data
        return get_response_data(
            model_id=model,
            provider_name="anthropic",
            input=prompt,
            status="error",
            error=str(e),
            p_tokens=p_tokens,
            c_tokens=c_tokens
        )