# ai_consensus_system_m1.py

import time
from functions.time_utils import get_current_time
from functions.log_generator import write_log
from constants.stage_names import (STAGE_0, STAGE_1, STAGE_1v, STAGE_2, STAGE_2v, STAGE_3, STAGE_3v, STAGE_4, STAGE_5)
import traceback

def run_ai_consensus_system_m1():
    try:
        # =========================
        # STAGE - 0 : Initial Setup
        # =========================

        # Initial log messages
        initial_log_messages = [f"AI_CONSENSUS_SYSTEM_M1 | START | AI_CONSENSUS_SYSTEM_M1_V1"]

        # Generate a unique request ID for tracking this full pipeline execution
        from functions.request_id_generator import generate_request_id
        request_id = generate_request_id(pre_log_messages=initial_log_messages)

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | START | {STAGE_0}")

        # Start high-precision timer (used for total execution duration)
        start_perf_counter = time.perf_counter()

        # Capture readable timestamp for when execution started
        start_timestamp = get_current_time()

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | SUCCESS | Start Timestamp captured", current_time=start_timestamp)

        # Fetch the base prompt (original user question)
        from hardcodes.prompt_manager import get_prompt
        base_prompt = get_prompt(request_id=request_id)


        # Load configured AI model settings (provider + model + key)
        from hardcodes.model_manager import get_models
        model_configurations = get_models(request_id=request_id)

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | END | {STAGE_0}")

        # ===================================
        # STAGE - 1 : Initial Model Execution
        # ===================================

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | START | {STAGE_1}")

        # Run all configured models with the base prompt (Round 1 - Generation)
        from functions.ai_orchestrator import run_models
        initial_model_outputs = run_models(
            prompt=base_prompt,
            models_data=model_configurations,
            request_id=request_id
        )

        # Save raw model responses to file for audit/debug purposes
        from functions.response_logger import save_response_log
        initial_response_log = save_response_log(
            request_id=request_id,
            prompt=base_prompt,
            outputs=initial_model_outputs,
            dir="outputs_m1/stage_01_initial",
        )

        # Convert raw responses into structured format: { model_name : output }
        from functions.response_formatter import format_structured_response
        initial_structured_result = format_structured_response(
            request_id=request_id,
            data=initial_response_log,
            dir="outputs_m1/stage_01_initial_structured",
        )

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | END | {STAGE_1}")

        # # ===================================================
        # # STAGE - 1.5 : Reload Initial Model Execution Output
        # # ===================================================

        # # Updating log entry 
        # write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | START | {STAGE_1v}")

        # # Hardcoded Request Id
        # request_id = "20260222_153248_709904"

        # # Load previously saved raw model responses (useful for replay/debug)
        # import json
        # with open(f"outputs_m1/stage_01_initial/{request_id}.json", "r") as file:
        #     initial_response_log = json.load(file)

        # # Display final combined raw model responses 
        # print(f"Initial Response Log:\n{initial_response_log}")

        # # Load previously saved structured result (useful for replay/debug)
        # import json
        # with open(f"outputs_m1/stage_01_initial_structured/{request_id}.json", "r") as file:
        #     initial_structured_result = json.load(file)

        # # Display final combined structured results
        # print(f"Initial Structured Result:\n{initial_structured_result}")

        # # Updating log entry 
        # write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | END | {STAGE_1v}")

        # ======================================
        # STAGE - 2 : Consensus Refinement Round
        # ======================================

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | START | {STAGE_2}")

        # Build a consensus prompt using all Stage-1 model outputs
        from functions.consensus_prompt_builder import build_consensus_prompt
        consensus_prompt = build_consensus_prompt(
            original_prompt=base_prompt,
            structured_result=initial_structured_result,
            request_id=request_id
        )

        # Execute models again using the consensus prompt (Round 2 - Refinement)
        consensus_model_outputs = run_models(
            prompt=consensus_prompt,
            models_data=model_configurations,
            request_id=request_id
        )

        # Save consensus round responses
        consensus_response_log = save_response_log(
            request_id=request_id,
            prompt=consensus_prompt,
            outputs=consensus_model_outputs,
            dir="outputs_m1/stage_02_consensus",
        )

        # Convert consensus responses into structured format
        consensus_structured_result = format_structured_response(
            request_id=request_id,
            data=consensus_response_log,
            dir="outputs_m1/stage_02_consensus_structured",
        )

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | END | {STAGE_2}")

        # # =========================================
        # # STAGE - 2.5 : Consensus Refinement Output
        # # =========================================

        # # Updating log entry 
        # write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | START | {STAGE_2v}")

        # # Load previously saved consensus round responses (useful for replay/debug)
        # import json
        # with open(f"outputs_m1/stage_02_consensus/{request_id}.json", "r") as file:
        #     consensus_response_log = json.load(file)

        # # Display final consensus round responses
        # print(f"Consensus Response Log:\n{consensus_response_log}")

        # # Load previously saved consensus structured result (useful for replay/debug)
        # import json
        # with open(f"outputs_m1/stage_02_consensus_structured/{request_id}.json", "r") as file:
        #     consensus_structured_result = json.load(file)

        # # Display final combined structured results
        # print(f"Consensus Structured Result:\n{consensus_structured_result}")

        # # Updating log entry 
        # write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | END | {STAGE_2v}")


        # ==================================
        # STAGE - 3 : Combined Scoring Round
        # ==================================

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | START | {STAGE_3}")

        # Build scoring prompt to evaluate consensus outputs
        from functions.combined_scoring_prompt_builder import build_combined_scoring_prompt
        scoring_prompt = build_combined_scoring_prompt(
            original_prompt=base_prompt,
            combined_structured_result=consensus_structured_result,
            request_id=request_id
        )

        # Execute scoring round (Round 3 - Evaluation)
        scoring_model_outputs = run_models(
            prompt=scoring_prompt,
            models_data=model_configurations,
            request_id=request_id
        )

        # Save raw scoring responses
        scoring_response_log = save_response_log(
            request_id=request_id,
            prompt=scoring_prompt,
            outputs=scoring_model_outputs,
            dir="outputs_m1/stage_03_scoring",
        )

        # Convert scoring outputs into structured format (model → JSON score string)
        scoring_structured_result = format_structured_response(
            request_id=request_id,
            data=scoring_response_log,
            dir="outputs_m1/stage_03_scoring_structured",
        )

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | END | {STAGE_3}")

        # # =========================================
        # # STAGE - 3.5 : Reload Scoring Round Output
        # # =========================================

        # # Updating log entry 
        # write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | START | {STAGE_3v}")

        # # Load previously saved raw scoring responses (useful for replay/debug)
        # import json
        # with open(f"outputs_m1/stage_03_scoring/{request_id}.json", "r") as file:
        #     scoring_response_log = json.load(file)

        # # Display final raw scoring responses
        # print(f"Scoring Response Log:\n{scoring_response_log}")

        # # Load previously saved scored structured result (useful for replay/debug)
        # import json
        # with open(f"outputs_m1/stage_03_scoring_structured/{request_id}.json", "r") as file:
        #     scoring_structured_result = json.load(file)

        # # Display final combined scores results
        # print(f"Scoring Structured Result:\n{scoring_structured_result}")

        # # Updating log entry 
        # write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | END | {STAGE_3v}")

        # =========================================
        # STAGE - 4 : Score Aggregation & Selection
        # =========================================

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | START | {STAGE_4}")

        # Parse stringified JSON score outputs into proper Python dictionary
        from functions.score_parser import parse_scoring_outputs
        parsed_score_matrix = parse_scoring_outputs(
            raw_scores=scoring_structured_result,
            request_id=request_id
        )

        # Save raw parsed score matrix (cross-model evaluation data)
        from functions.score_logger import save_scores_log
        save_scores_log(
            request_id=request_id,
            scores=parsed_score_matrix,
            dir="outputs_m1/stage_04_raw_scores",
        )

        # Aggregate scores across evaluators (optionally remove self-scoring bias)
        from functions.score_aggregator import aggregate_model_scores
        aggregated_scores = aggregate_model_scores(
            parsed_scores=parsed_score_matrix,
            # remove_self_bias=False,
            remove_self_bias=True,
            request_id=request_id
        )

        # Save aggregate weighted scores for audit
        save_scores_log(
            request_id=request_id,
            scores=aggregated_scores,
            dir="outputs_m1/stage_04_aggregated_scores"
        )

        # Calculate weighted final score per model
        from functions.final_score_calculator import calculate_weighted_score
        weighted_scores = calculate_weighted_score(
            agent_scores=aggregated_scores, 
            request_id=request_id
        )

        # Save final weighted scores for audit
        save_scores_log(
            request_id=request_id,
            scores=weighted_scores,
            dir="outputs_m1/stage_04_weighted_scores"
        )

        # Select winning model based on highest weighted score
        from functions.winner_selector import select_winner
        winning_model = select_winner(
            final_scores=weighted_scores,
            combined_model_outputs=consensus_model_outputs,
            request_id=request_id
        )

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | END | {STAGE_4}")

        # =======================================
        # STAGE - 5 : Report Generation & Logging
        # =======================================

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | START | {STAGE_5}")

        # Stop performance timer
        end_perf_counter = time.perf_counter()

        # Capture readable end timestamp
        end_timestamp = get_current_time()

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | SUCCESS | End Timestamp captured", current_time=end_timestamp)

        # Calculate total pipeline execution time (in seconds)
        total_execution_time = round(end_perf_counter - start_perf_counter, 4)

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | SUCCESS | Total pipeline execution time {total_execution_time} seconds")

        # Save final winning result along with metadata and timing info
        from functions.winner_logger import save_winner_log
        save_winner_log(
            request_id=request_id,
            prompt=base_prompt,
            model=winning_model["model"],
            score=winning_model["score"],
            output=winning_model["output"],
            start_time=start_timestamp,
            end_time=end_timestamp,
            execution_time=total_execution_time,
            dir="outputs_m1/stage_05_winner"
        )

        # Generate stage-wise and overall token usage summary for this request
        from functions.token_summary_generator import generate_token_summary
        token_summary = generate_token_summary(
            request_id=request_id,
            stage1_output_data=initial_response_log.get("outputs"),
            stage2_output_data=consensus_response_log.get("outputs"),
            stage3_output_data=scoring_response_log.get("outputs"),
            directory="outputs_m1/stage_05_token_summary"
        )

        # Generate stage-wise and model-wise token report DataFrames
        from functions.token_report_builder import build_token_reports
        stage_token_report_df, model_summary_token_report_df = build_token_reports(
            request_id=request_id,
            token_summary_data=token_summary
        )


        # Export stage-wise token report as CSV
        from functions.csv_exporter import export_csv
        export_csv(
            request_id=request_id,
            data=stage_token_report_df,
            directory="outputs_m1/stage_05_token_report_stage"
        )

        # Export model-wise token summary report as CSV
        export_csv(
            request_id=request_id,
            data=model_summary_token_report_df,
            directory="outputs_m1/stage_05_token_report_model_summary"
        )

        # Updating log entry 
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | END | {STAGE_5}")

    except Exception as e:
        
        # Capture full traceback
        error_trace = traceback.format_exc()

        # Log fatal error
        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | FAILED | Error in main.py file")
        write_log(filename=request_id, message=f"ERROR : {str(e)}")

        write_log(filename=request_id, message=f"AI_CONSENSUS_SYSTEM_M1 | TRACEBACK | Tracebacking error")
        write_log(filename=request_id, message=f"ERROR : {error_trace}")

        # Optional: re-raise if you want program to stop
        raise