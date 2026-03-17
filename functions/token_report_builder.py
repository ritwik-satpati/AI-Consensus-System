# token_report_builder.py
MODULE_NAME = "TOKEN_REPORT_BUILDER"

import pandas as pd
from functions.log_generator import write_log


def build_token_reports(request_id, token_summary_data):
    """
    Builds two DataFrames:
    1. Stage-wise model breakdown
    2. Model-wise overall summary (ALL_STAGES)
    """

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | START | Token report building initiated")

    # Convert JSON list to DataFrame
    df = pd.DataFrame(token_summary_data)

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Token summary converted to DataFrame")

    # ============================
    # Stage-wise breakdown
    # ============================

    stage_df = df[
        (df["stage"] != "ALL_STAGES")
    ][
        ["stage", "provider", "model", "prompt_token", "completion_token", "total_token"]
    ]

    stage_df = stage_df.reset_index(drop=True)

    print(f"Stage DF :\n{stage_df}")

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Stage-wise report generated")

    # ============================
    # Model-wise overall summary
    # ============================

    model_summary_df = df[
        (df["stage"] == "ALL_STAGES") &
        (df["model"] != "ALL_MODELS")
    ][
        ["provider", "model", "prompt_token", "completion_token", "total_token"]
    ]

    model_summary_df = model_summary_df.reset_index(drop=True)

    print(f"Model Summary DF :\n{model_summary_df}")

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Model-wise summary report generated")

    # Updating log entry
    write_log(filename=request_id, message=f"{MODULE_NAME} | SUCCESS | Token report building completed")

    return stage_df, model_summary_df