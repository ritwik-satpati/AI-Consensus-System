# model_manager.py

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
        get_api_data(company_name="openai", model_id="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")),
        # get_api_data(company_name="google", model_id="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),
        get_api_data(company_name="google", model_id="gemini-2.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY")),
        # get_api_data(company_name="anthropic", model_id="claude-sonnet-4-6", api_key=os.getenv("ANTHROPIC_API_KEY")),
        get_api_data(company_name="anthropic", model_id="claude-haiku-4-5-20251001", api_key=os.getenv("ANTHROPIC_API_KEY")),
        get_api_data(company_name="deepseek", model_id="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY")),
    )

    # Updating log entry 
    write_log(filename=request_id, message=f"MODEL_MANAGER | SUCCESS | AI model configurations loaded")

    # Return structured Models data
    return models