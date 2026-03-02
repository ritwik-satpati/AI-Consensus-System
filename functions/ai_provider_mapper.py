# ai_provider_mapper.py

# ai_orchestrator.py

# Import provider-specific API call functions
from api.openai_api import call_openai
from api.gemini_api import call_gemini
from api.claude_api import call_claude
from api.deepseek_api import call_deepseek


def mapping_ai_provider():

    # Map provider name to its corresponding function
    provider_map = {
        "openai": call_openai,
        "google": call_gemini,
        "anthropic":  call_claude,
        "deepseek": call_deepseek
    }

    return provider_map