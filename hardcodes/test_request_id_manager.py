# test_request_id_manager.py
MODULE_NAME = "TEST_REQUEST_ID_MANAGER"

from functions.log_generator import write_log


def get_test_request_id():
    """
    This function returns a hardcoded test request_id (used for replay/debug)
    """
    
    test_request_id = None
    # test_request_id = "20260322_011922_308983"
    
    if test_request_id:
        # Updating log entry 
        write_log(filename=test_request_id, message=f"{MODULE_NAME} | SUCCESS | Test Request Id loaded")

    return test_request_id