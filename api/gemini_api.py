# gemini_api.py
MODULE_NAME = "GEMINI_API"

from google import genai
from dotenv import load_dotenv
from models.response_data import get_response_data
from functions.log_generator import write_log


# Load environment variables
load_dotenv()


async def call_gemini(prompt, model, key, system_prompt, request_id):
    """
    This function sends a prompt to Gemini and returns the response
    """    
    
    # Create Gemini client using the API key from .env
    client = genai.Client(api_key=key)

    try:
        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | START | Request initiated | {model}")

        # API Call
        response = await client.aio.models.generate_content(
            model=model,
            config={"system_instruction": system_prompt},
            contents=prompt
        )

        # # Print the response
        # print(response)

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Response received | {model} | Prompt Tokens = {response.usage_metadata.prompt_token_count} | Completion Tokens = {response.usage_metadata.candidates_token_count}")

        # Return Success Data
        return get_response_data(
            model_id=model,
            provider_name="google",
            input=prompt,
            output=response.text,
            p_tokens=response.usage_metadata.prompt_token_count,
            c_tokens=response.usage_metadata.candidates_token_count,
            status="success"
        )

    except Exception as e:
        # Fallback token extraction if the API failed midway
        p_tokens = 0
        c_tokens = 0
        if 'response' in locals() and hasattr(response, 'usage_metadata') and response.usage_metadata:
            p_tokens = response.usage_metadata.prompt_token_count or 0
            c_tokens = response.usage_metadata.candidates_token_count or 0

        # Updating log entry 
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Error during API call | {model} | Prompt Tokens = {p_tokens} | Completion Tokens = {c_tokens}")
        write_log(filename=request_id, message=f"ERROR : {str(e)}'")
        
        # Return Error Data
        return get_response_data(
            model_id=model,
            provider_name="google",
            input=prompt,
            status="error",
            error=str(e),
            p_tokens=p_tokens,
            c_tokens=c_tokens
        )