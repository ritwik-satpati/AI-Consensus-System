# nvidia_api.py
MODULE_NAME = "NVIDIA_API"

from openai import AsyncOpenAI
from dotenv import load_dotenv
from models.response_data import get_response_data
from functions.log_generator import write_log

# Load environment variables
load_dotenv()


async def call_nvidia(prompt, model, key, system_prompt, request_id):
    """
    This function sends a prompt to NVIDIA NIM model and returns structured response data
    """
    
    client = AsyncOpenAI(
        api_key=key,
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
            ],
            temperature=1,
            max_tokens=1024,
            top_p=0.95,
            extra_body={
                "chat_template_kwargs": {"enable_thinking": False},
                "reasoning_budget": 512
            }
        )

        # Extract output
        output_text = response.choices[0].message.content

        # Updating log entry
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Response received | {model} | Prompt Tokens = {response.usage.prompt_tokens} | Completion Tokens = {response.usage.completion_tokens}")

        # Return success data
        return get_response_data(
            model_id=model,
            provider_name="nvidia",
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
        
        print(e)

        # Return error data
        return get_response_data(
            model_id=model,
            provider_name="nvidia",
            input=prompt,
            status="error",
            error=str(e),
            p_tokens=p_tokens,
            c_tokens=c_tokens
        )