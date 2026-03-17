# AI Consensus System - M1

This document outlines the technical architecture and data flow of the Multi-Model Orchestration Pipeline. The system is designed as a **Sequential Multi-Agent Consensus** engine, where multiple LLMs compete, refine, and peer-evaluate to reach a high-quality "Winning" output.

## 📋 Linear Data Flow Summary

This is the end-to-end journey of a single request through the pipeline:

**Input Prompt** $\Rightarrow$ **Input Models & Keys** $\Rightarrow$ **Generate request_id & Initialize Logs** $\Rightarrow$ **Start Time Counting** $\Rightarrow$

**Send for Output to Each Model** $\Rightarrow$ **Output Captured & Structured** $\Rightarrow$

**[Reload/Inspect Stage 1]** $\Rightarrow$

**Output Combined into Consensus Prompt** $\Rightarrow$ **Send Combined Output to All Models** $\Rightarrow$ **Consensus Output Captured & Structured** $\Rightarrow$

**[Reload/Inspect Stage 2]** $\Rightarrow$

**Send Consensus Outputs to All for Scoring** $\Rightarrow$ **Score Output Captured & Structured** $\Rightarrow$

**[Reload/Inspect Stage 3]** $\Rightarrow$

**Captured Scores Formatted in JSON & Saved** $\Rightarrow$ **Aggregate Scores (Self-Bias Removal Enabled)** $\Rightarrow$ **Weighted Score Calculation (Internal Weightage System)** $\Rightarrow$ **Winner Model Selected** $\Rightarrow$

**Stop Time Counting** $\Rightarrow$ **Execution Metrics Calculated** $\Rightarrow$ **Winner Data Saved** $\Rightarrow$ **Token Summary Generated** $\Rightarrow$ **Stage-wise & Model-wise CSV Reports Exported**

---

## 🔄 Detailed Stage Breakdown

### **STAGE 0 | Initial Setup**

- **Input:** User prompt and model configuration list.
- **Logic:**
  - Generates a unique `request_id`.
  - Initializes log entries.
  - Starts high-precision performance counter using `time.perf_counter()`.
  - Captures readable start timestamp via `get_current_time()`.
  - Loads:
    - `base_prompt`
    - `model_configurations`

- **Status:** Stage start and end logs recorded under the same `request_id`.

---

### **STAGE 1 | Initial Model Execution**

- **Input:** `base_prompt` + `model_configurations`.
- **Logic:**
  - Sends the prompt to each configured model using `run_models()`.
  - Captures raw responses.

- **Output Captured & Structured:**
  - Raw responses saved to:

    ```
    outputs/stage_01_initial/
    ```

  - Structured responses generated via `format_structured_response()` and saved to:

    ```
    outputs/stage_01_initial_structured/
    ```

- **Purpose:** Establishes independent first-pass responses from each model.

> **🔍 STAGE 1.5 | Reload Initial Output (Optional/Debug)**
>
> - Allows reloading of previously saved raw or structured outputs from disk.
> - Skips API calls during debugging or replay scenarios.

---

### **STAGE 2 | Consensus Refinement**

- **Input:** `base_prompt` + Combined structured output from Stage 1.
- **Logic:**
  - Builds a consensus prompt using `build_consensus_prompt()`.
  - Sends refined prompt to all models again.

- **Output Captured & Structured:**
  - Raw consensus responses saved to:

    ```
    outputs/stage_02_consensus/
    ```

  - Structured consensus results saved to:

    ```
    outputs/stage_02_consensus_structured/
    ```

- **Purpose:** Improves answer quality using collective reasoning.

> **🔍 STAGE 2.5 | Consensus Refinement Output (Optional/Debug)**
>
> - Allows inspection or reload of consensus-stage outputs.
> - Useful for validating refinement behavior before scoring.

---

### **STAGE 3 | Scoring Round**

- **Input:** All refined outputs from Stage 2.
- **Logic:**
  - Builds scoring prompt via `build_combined_scoring_prompt()`.
  - Each model evaluates all consensus outputs.
  - Creates a cross-model evaluation matrix.

- **Score Output Captured & Structured:**
  - Raw scoring responses saved to:

    ```
    outputs/stage_03_scoring/
    ```

  - Structured scoring results saved to:

    ```
    outputs/stage_03_scoring_structured/
    ```

> **🔍 STAGE 3.5 | Reload Scoring Round Output (Optional/Debug)**
>
> - Reloads raw or structured scoring results.
> - Enables inspection of individual judge behavior.

---

### **STAGE 4 | Score Aggregation & Selection**

- **Process:**

1. **Parse:**
   - Converts stringified scoring JSON into Python dictionaries using `parse_scoring_outputs()`.
   - Saved to:

     ```
     outputs/stage_04_raw_scores/
     ```

2. **Aggregation:**
   - Aggregates peer scores using `aggregate_model_scores()`.
   - `remove_self_bias=True` is enabled to eliminate self-scoring bias.
   - Saved to:

     ```
     outputs/stage_04_aggregated_scores/
     ```

3. **Internal Weightage System:**
   - Applies final weighted scoring using `calculate_weighted_score()`.
   - Weighted results saved to:

     ```
     outputs/stage_04_weighted_scores/
     ```

- **Winner Selected:**
  - `select_winner()` chooses the model with the highest weighted score.
  - Winning model includes:
    - Model name
    - Final score
    - Consensus output

---

### **STAGE 5 | Finalization & Logging**

- **Action:**

1. **Stop Time Counting:**
   - Stops performance counter.
   - Captures end timestamp via `get_current_time()`.

2. **Execution Metrics:**
   - Calculates total execution time in seconds.
   - Logs full pipeline duration.

3. **Winner Logging:**
   - Saves winning model details to:

     ```
     outputs/stage_05_winner/
     ```

   - Includes:
     - Prompt
     - Model name
     - Final score
     - Output
     - Start time
     - End time
     - Execution time

4. **Token Summary Generation:**
   - `generate_token_summary()` computes:
     - Stage 1 token usage
     - Stage 2 token usage
     - Stage 3 token usage

   - Saved to:

     ```
     outputs/stage_05_token_summary/
     ```

5. **Token Report DataFrames:**
   - `build_token_reports()` generates:
     - Stage-wise token report
     - Model-wise token summary report

6. **CSV Export:**
   - `export_csv()` saves reports to:

     ```
     outputs/stage_05_token_report_stage/
     outputs/stage_05_token_report_model_summary/
     ```

- **Result:** Fully logged, measurable, auditable AI decision pipeline.

---

## 🛠️ Design Principles

### **1. Persistent State Checkpoints**

Unlike a standard memory-only script, this architecture saves the state to the file system at every stage (`outputs/stage_xx_...`). This allows for:

- **Auditability:** You can see exactly why a model won.
- **Resiliency:** If a stage fails, the data from previous stages is preserved.

### **2. Internal Weightage System with Bias Control**

The winner isn't chosen by a single model, but by the weighted average of the entire "judge panel." This mitigates hallucinations and promotes logical consistency.

### **3. Token Cost Observability**

Stage-wise and model-wise token reports provide:

- Cost transparency
- Performance comparison
- Optimization opportunities

### **4. Error & Traceback Management**

The system is wrapped in a global **try-except** block. If any step fails, the system:

- **Captures the full traceback** via `traceback.format_exc()`.
- **Logs the specific failure** to the unique `request_id` log file.
- **Ensures that the developer knows exactly which step in the chain caused the interruption**, making debugging significantly faster.

---
