# stage_wrapper.py
MODULE_NAME = "STAGE_WRAPPER"

import time
from functions.log_generator import write_log
from functions.time_utils import get_current_time
from functions.output_manager import update_output_file


def stage_wrapper(stage_name):
    """
    This decorator wraps stage execution.

    - Adds stage-level logging (START / SUCCESS / FAILED)
    - Tracks execution time for each stage
    - Stores stage timing in context
    """

    def decorator(func):

        async def wrapper(context, *args, **kwargs):
            
            # Start high-precision timer
            start = time.perf_counter()
            
            # Capture start timestamp
            start_timestamp = get_current_time()

            # Capture current stage
            context.current_stage = stage_name

            # Safe request_id (works for setup stage as well)
            request_id = getattr(context, "request_id", "INIT")

            # Updating log entry 
            write_log(filename=request_id, message=f"{MODULE_NAME} | START | {stage_name}")
            
            try:
                # Execute actual stage function
                result = await func(context, *args, **kwargs)
                status = "END"

            except Exception as e:
                status = "FAILED"

                # Updating log entry
                write_log(filename=request_id, message=f"ERROR : {str(e)}")

                raise

            finally:
                # Capture start timestamp
                end_timestamp = get_current_time()

                # Stop timer
                end = time.perf_counter()
                duration = round(end - start, 4)

                # Re-fetch request_id (important for setup stage)
                request_id = getattr(context, "request_id", request_id)

                # # Store timing in context
                # if not hasattr(context, "stage_timings"):
                #     context.stage_timings = {}

                # context.stage_timings[stage_name] = duration

                # Capture Stage Data (safe copy to avoid mutation issues)
                stage_data = dict(context.current_stage_data or {})

                # Add stage timing
                stage_data["startedAt"] = start_timestamp
                stage_data["completedAt"] = end_timestamp
                stage_data["stage_timing"] = duration

                # Save the output 
                update_output_file(
                    request_id=context.request_id,
                    stage_name=context.current_stage,
                    stage_data=stage_data
                )

                # Updating log entry 
                write_log(filename=request_id, message=f"{MODULE_NAME} | {status} | {stage_name} | Step execution time {duration} seconds")

            return result

        return wrapper

    return decorator