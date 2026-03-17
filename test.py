# test.py
MODULE_NAME = "TEST"

from functions.log_generator import write_log
from dotenv import load_dotenv
from functions.log_generator import write_log

# Load environment variables from .env file
load_dotenv()

def test():

    # Hardcoded request_id & prompts
    request_id = "XXXX_XXXXXX_XXXXXX"
    base_prompt = "Explain API in simple words within 100 words"
    system_prompt = "You are a helpful assistant."

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | START | Used for replay/debug")

    print("This is for internal Tesing!")
    
    # Tesing code - Start
    
    pass
    
    # Tesing code - End

    # Updating log entry 
    write_log(filename=request_id, message=f"{MODULE_NAME} | END | Used for replay/debug")

    return True