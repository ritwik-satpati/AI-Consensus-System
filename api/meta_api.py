# meta_api.py
MODULE_NAME = "META_API"

from openai import AsyncOpenAI
from dotenv import load_dotenv
from models.response_data import get_response_data
from functions.log_generator import write_log


# Load environment variables
load_dotenv()


async def call_meta(prompt, model, key, system_prompt, request_id):
    """
    This function sends a prompt to Meta Llama model and returns structured response data
    """
    
    # Together AI uses OpenAI compatible API
    client = AsyncOpenAI(
        api_key=key,
        # base_url="https://api.together.xyz/v1"
        base_url="https://integrate.api.nvidia.com/v1"
    )

    response = None

    try:

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | START | Request initiated | {model}")

        # API Call
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract output
        output_text = response.choices[0].message.content

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Response received | {model} | Prompt Tokens = {response.usage.prompt_tokens} | Completion Tokens = {response.usage.completion_tokens}")

        # Return Success Data
        return get_response_data(
            model_id=model,
            provider_name="meta",
            input=prompt,
            output=output_text,
            p_tokens=response.usage.prompt_tokens,
            c_tokens=response.usage.completion_tokens,
            status="success"
        )

    except Exception as e:

        p_tokens = 0
        c_tokens = 0

        if response and hasattr(response, "usage") and response.usage:
            p_tokens = response.usage.prompt_tokens or 0
            c_tokens = response.usage.completion_tokens or 0

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Error during API call | {model} | Prompt Tokens = {p_tokens} | Completion Tokens = {c_tokens}")
        write_log(filename=request_id, message=f"ERROR : {str(e)}")

        return get_response_data(
            model_id=model,
            provider_name="meta",
            input=prompt,
            status="error",
            error=str(e),
            p_tokens=p_tokens,
            c_tokens=c_tokens
        )