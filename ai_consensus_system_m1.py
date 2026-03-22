# ai_consensus_system_m1.py
MODULE_NAME = "AI_CONSENSUS_SYSTEM_M1"

import traceback
from functions.log_generator import write_log
from pipeline_context import PipelineContext


async def run_ai_consensus_system_m1():
    """
    This function orchestrates the full AI Consensus System pipeline.

    - Initializes pipeline context
    - Executes all stages sequentially
    - Handles errors and logs failures

    Stage-level logging, timing, and execution tracking are managed by individual stage wrappers.
    """

    context = PipelineContext()

    try:
        # =========================
        # PIPELINE EXECUTION FLOW
        # =========================

        # ===== STAGE - Initial System Setup =====
        from stages.system_setup import run_system_setup
        await run_system_setup(context)

        # ===== STAGE - Initial Model Execution =====
        from stages.initial_execution import run_initial_execution
        await run_initial_execution(context)

        # # ===== STAGE - Reload Initial Model Execution Output =====
        # from stages.initial_execution_reload import run_initial_execution_reload
        # await run_initial_execution_reload(context, isPrint=False)

        # ===== STAGE - Combined Consensus Synthesis =====
        from stages.consensus_synthesis import run_consensus_synthesis
        await run_consensus_synthesis(context)

        # # # ===== STAGE - Reload Combined Consensus Synthesis Output =====
        # from stages.consensus_synthesis_reload import run_consensus_synthesis_reload
        # await run_consensus_synthesis_reload(context, isPrint=False)

        # ===== STAGE - Combined Scoring Round =====
        from stages.scoring_combined import run_scoring_combined
        await run_scoring_combined(context)

        # # ===== STAGE - Reload Combined Scoring Round Output =====
        # from stages.scoring_combined_reload import run_scoring_combined_reload
        # await run_scoring_combined_reload(context, isPrint=False)

        # ===== STAGE - Score Aggregation =====
        from stages.score_aggregation import run_score_aggregation
        await run_score_aggregation(context)

        # ===== STAGE - Winner Selection =====
        from stages.winner_selection import run_winner_selection
        await run_winner_selection(context)        

        # ===== STAGE - Report Generation & Logging =====
        from stages.report_generation import run_report_generation
        await run_report_generation(context, isPrint=True)

    except Exception as e:

        # Capture full traceback
        error_trace = traceback.format_exc()

        request_id = getattr(context, "request_id", "UNKNOWN")

        # Log fatal error
        write_log(filename=request_id, message=f"{MODULE_NAME} | FAILED | Pipeline execution failed")
        write_log(filename=request_id, message=f"ERROR : {str(e)}")

        write_log(filename=request_id, message=f"{MODULE_NAME} | TRACEBACK")
        write_log(filename=request_id, message=f"ERROR : {error_trace}")

        raise