# AI Consensus System - V 1.0

A robust Python-based orchestration pipeline that leverages multiple LLMs to generate, refine, and peer-evaluate responses. The system ensures that the final output is not produced by a single model, but emerges from a structured multi-stage consensus and scoring process.

---

## 🚀 Overview

The AI Consensus System is built on the principle that multiple independent reasoning agents can collectively produce more reliable results than a single model.

The project currently includes **two scoring architectures**:

- **M1 – Full Cross Scoring Architecture**
- **M2 – Randomized One-to-One Scoring Architecture**

Both follow the same generation and consensus stages but differ in how Stage 3 (Scoring) is executed.

📄 Detailed documentation:

- **AI Consensus System – M1 - V1 - Version 1.0.0** $\Rightarrow$ [AI Consensus System – M1 Architecture](./AI_Consensus_System_M1.md)
- **AI Consensus System – M2 - V1 - Version 1.0.0** $\Rightarrow$ [AI Consensus System – M2 Architecture](./AI_Consensus_System_M2.md)
- [M1 vs M2 Comparison](./AI_Consensus_System_M1_vs_M2.md)

---

## ✨ Key Features

- **Multi-Model Orchestration**
  Supports multiple AI providers (OpenAI, Google Gemini, Anthropic, etc.) within a unified pipeline.

- **Iterative Consensus Refinement**
  Uses a multi-round generation approach (Initial → Consensus).

- **Structured Peer Evaluation**
  Models act as evaluators for other model outputs.

- **Multiple Scoring Architectures**
  Choose between:
  - M1 (Full Cross Evaluation)
  - M2 (Randomized Blind Peer Evaluation)

- **Weighted Scoring System**
  Applies mathematical aggregation with optional self-bias removal.

- **Execution Tracking**
  Captures request-level timestamps and total execution time.

- **Comprehensive Logging & Auditability**
  Every stage stores raw and structured outputs for traceability.

- **Token Usage Reporting**
  Generates stage-wise and model-wise token reports with CSV export.

---

## 🛠 Execution Flow (Common to M1 & M2)

1. **Initial Setup**
   - Generates unique `request_id`
   - Captures execution timestamps
   - Loads prompt and model configuration

2. **Initial Model Execution**
   - Sends base prompt to all configured models
   - Captures and structures raw outputs

3. **Consensus Refinement**
   - Builds a combined consensus prompt
   - Produces refined outputs from all models

4. **Scoring & Evaluation**
   - M1: Full cross-model scoring
   - M2: Randomized one-to-one scoring

5. **Aggregation & Winner Selection**
   - Applies weighted scoring logic
   - Selects highest-ranked output

6. **Finalization**
   - Logs execution metrics
   - Saves winner data
   - Exports token reports

---

## 📁 Directory Structure

The system organizes outputs into structured directories:

| Directory                                      | Content                                    |
| ---------------------------------------------- | ------------------------------------------ |
| `outputs/stage_01_initial/`                    | Raw JSON responses from initial generation |
| `outputs/stage_01_initial_structured/`         | Structured `{model: output}` mappings      |
| `outputs/stage_02_consensus/`                  | Refined consensus outputs                  |
| `outputs/stage_03_scoring/`                    | Raw scoring responses                      |
| `outputs/stage_04_raw_scores/`                 | Parsed scoring matrices                    |
| `outputs/stage_04_weighted_scores/`            | Final weighted standings                   |
| `outputs/stage_05_winner/`                     | Final winning output + metadata            |
| `outputs/stage_05_token_summary/`              | Token usage breakdown                      |
| `outputs/stage_05_token_report_stage/`         | Stage-wise token CSV                       |
| `outputs/stage_05_token_report_model_summary/` | Model-wise token CSV                       |

---

## 📝 Usage

### Prerequisites

Tested with:

- **Python 3.13.12**
- **pip 26.0.1**

---

### Installation

```bash
pip install python-dotenv
pip install openai
pip install -U google-genai
pip install anthropic
```

---

### Configuration

Create a `.env` file:

```bash
# OpenAI API key used by the OpenAI client
OPENAI_API_KEY=XXXXX

# Google Gemini API key used by the Gemini client
GEMINI_API_KEY=XXXXX

# Claude API key used by the Claude client
ANTHROPIC_API_KEY=xxxxx

# Deepseek API key used by the Deepseek client
DEEPSEEK_API_KEY=xxxxxx
```

Configure:

- `hardcodes/model_manager.py`
- `hardcodes/prompt_manager.py`

---

### Execution

```bash
python main.py
```

---

Perfect 👍 we’ll add a clean **Supported AI Providers** section at the end of your `README.md`.

Here’s the section you can append at the bottom:

---

## 🤖 Supported AI Providers

The AI Consensus System currently supports multiple AI providers through modular client integrations:

- **OpenAI**
- **Google Gemini**
- **Anthropic (Claude)**
- **DeepSeek**
