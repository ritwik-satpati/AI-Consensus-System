# test.py

from functions.log_generator import write_log
from api.deepseek_api import call_deepseek
# Import
import os
from dotenv import load_dotenv
from models.api_data import get_api_data
from functions.log_generator import write_log


# Load environment variables from .env file
load_dotenv()

def test():

    # Hardcoded request_id & original_prompt
    request_id = "XXXX_214848_791687"
    original_prompt = "Explain API in simple words within 100 words"

    # Updating log entry 
    write_log(filename=request_id, message=f"TEST | START | Used for replay/debug")


    resposne = call_deepseek(
        prompt=original_prompt, 
        model="deepseek-chat", 
        key=os.getenv("DEEPSEEK_API_KEY"), 
        request_id=request_id
    )

    print(resposne)

    # Updating log entry 
    write_log(filename=request_id, message=f"TEST | END | Used for replay/debug")


    return True