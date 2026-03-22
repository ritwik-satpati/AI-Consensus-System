# report_generation.py
MODULE_NAME = "REPORT_GENERATION"

from functions.stage_wrapper import stage_wrapper


@stage_wrapper(MODULE_NAME)
async def run_report_generation(context, isPrint=False):
    """
    This function performs final report generation and logging.

    - Generates token usage summary
    - Builds token usage reports
    - Exports reports as CSV files

    All logging, request_id handling, and execution tracking are managed by the stage wrapper.
    """

    # Import required modules for reporting stage execution
    from functions.token_summary_generator import generate_token_summary
    from functions.token_report_builder import build_token_reports
    from functions.csv_exporter import export_csv


    # Generate stage-wise and overall token usage summary
    token_summary = generate_token_summary(
        request_id=context.request_id,
        stages_output_data=context.stages_output,
        # directory="outputs/token_summary"
    )

    # Generate stage-wise and model-wise token report DataFrames
    stage_token_report, model_token_report = build_token_reports(
        request_id=context.request_id,
        token_summary_data=token_summary
    )

    # Export stage-wise token report as CSV
    export_csv(
        request_id=context.request_id,
        data=stage_token_report,
        dataframe_label="Stage DF",
        isPrint=isPrint,
        directory="outputs/token_report_stage"
    )

    # Export model-wise token summary report as CSV
    export_csv(
        request_id=context.request_id,
        data=model_token_report,
        dataframe_label="Model DF",
        isPrint=isPrint,
        directory="outputs/token_report_model"
    )

    # Capture current satge data
    context.current_stage_data={
        "token_summary":token_summary,
        "stage_token_report": stage_token_report,
        "model_token_report": model_token_report
    }