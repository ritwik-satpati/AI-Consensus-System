# ai_provider_mapper.py
MODULE_NAME = "AI_PROVIDER_MAPPER"

# Import provider-specific API call functions
from api.openai_api import call_openai
from api.gemini_api import call_gemini
from api.claude_api import call_claude
from api.deepseek_api import call_deepseek
from api.nvidia_api import call_nvidia
from api.grok_api import call_grok
from api.meta_api import call_meta
from api.mistral_api import call_mistral


def mapping_ai_provider():
    """
    This function connect ai api name to its corresponding function using provider_map
    """
    
    # Map provider name to its corresponding function
    provider_map = {
        "openai": call_openai,
        "google": call_gemini,
        "anthropic":  call_claude,
        "deepseek": call_deepseek,
        "nvidia": call_nvidia,
        "xai": call_grok,
        "meta": call_meta,
        "mistral": call_mistral
    }

    return provider_map