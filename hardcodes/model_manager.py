# model_manager.py
MODULE_NAME = "MODEL_MANAGER"

# Import
import os
from dotenv import load_dotenv
from models.api_data import get_api_data
from functions.log_generator import write_log


# Load environment variables from .env file
load_dotenv()

# This function manages which API configuration to use
def get_models(request_id):

    models = (
        get_api_data(provider_name="openai", model_id="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")),
        # get_api_data(provider_name="google", model_id="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),
        get_api_data(provider_name="google", model_id="gemini-2.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY")),
        # get_api_data(provider_name="anthropic", model_id="claude-sonnet-4-6", api_key=os.getenv("ANTHROPIC_API_KEY")),
        get_api_data(provider_name="anthropic", model_id="claude-haiku-4-5-20251001", api_key=os.getenv("ANTHROPIC_API_KEY")),
        # get_api_data(provider_name="deepseek", model_id="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY")),
        get_api_data(provider_name="nvidia", model_id="nvidia/nemotron-3-super-120b-a12b", api_key=os.getenv("NVIDIA_API_KEY")),
        # get_api_data(provider_name="xai", model_id="grok-4-1-fast-reasoning", api_key=os.getenv("XAI_API_KEY")),
        # get_api_data(provider_name="meta", model_id="meta-llama/Llama-3.1-8B-Instruct", api_key=os.getenv("META_API_KEY")),
        get_api_data(provider_name="meta", model_id="meta/llama-4-maverick-17b-128e-instruct", api_key=os.getenv("META_API_KEY")),
        get_api_data(provider_name="mistral", model_id="mistral-small-latest", api_key=os.getenv("MISTRAL_API_KEY")),
    )

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | AI model configurations loaded")

    # Return structured Models data
    return models