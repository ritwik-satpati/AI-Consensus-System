# AI Consensus System - V3 - Version 1.2.0

A robust Python-based orchestration pipeline that leverages multiple LLMs to generate, refine, and peer-evaluate responses. The system ensures that the final output is not produced by a single model, but emerges from a structured multi-stage consensus and scoring process.

---

## 🚀 Overview

The AI Consensus System is built on the principle that multiple independent reasoning agents can collectively produce more reliable results than a single model.

The project currently includes **two scoring architectures**:

- **M1 – Full Cross Scoring Architecture**
- **M2 – Randomized One-to-One Scoring Architecture**

Both follow the same generation and consensus stages but differ in how Stage 3 (Scoring) is executed.

### 📄 Detailed documentation

- **AI Consensus System – M1 - V3 - Version 1.2.0** $\Rightarrow$ [AI Consensus System – M1 Architecture](./docs/AI_Consensus_System_M1.md)
- **AI Consensus System – M2 - V3 - Version 1.2.0** $\Rightarrow$ [AI Consensus System – M2 Architecture](./docs/AI_Consensus_System_M2.md)
- [M1 vs M2 Comparison](./docs/AI_Consensus_System_M1_vs_M2.md)

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

5. **Score Aggregation**
   - Computes aggregated and weighted scores from model evaluations  

6. **Winner Selection**
   - Selects the final output based on highest-ranked score  
   - Saves some more details about the pipeline

7. **Finalization**
   - Logs execution metrics  
   - Saves consolidated output  
   - Generates token usage summary  

---

## 📁 Directory Structure

```
AI-CONSENSUS-SYSTEM/
│
├── main.py                         # Entry point for execution
│
├── ai_consensus_system_m1.py       # M1 pipeline (Full Cross Scoring)
├── ai_consensus_system_m2.py       # M2 pipeline (Randomized Scoring)
├── test.py                         # Testing utilities / scripts
│
├── stages/                         # Modular pipeline stages (reusable across M1 & M2)
├── pipeline_context.py             # Centralized pipeline state management
│
├── api/                            # API integrations for different AI providers
├── functions/                      # Core reusable utility functions
├── models/                         # Data models and schemas
├── hardcodes/                      # Static configurations (models, prompts, etc.)
│
├── logs/                           # Execution logs and trace files (.log)
├── outputs/                        # Pipeline output artifacts
│   ├── <request_id>.json           # Consolidated pipeline output (JSON)
│   ├── token_report_model/         # Model-wise token usage reports (CSV)
│   ├── token_report_stage/         # Stage-wise token usage reports (CSV)
│   └── <custom_folder>/            # Optional: specific outputs
│       └── <request_id>.json       # Specific output (JSON)
│
├── .env                            # Environment variables (API keys)
├── .env.sample                     # Sample environment configuration
├── .gitignore                      # Git ignore rules
│
├── docs/                           # Detailed architecture and comparison documents
├── CHANGELOG.md                    # Version history and updates
├── Limitations.md                  # Known limitations and constraints
├── README.md                       # Project documentation
```
> **Note:** The system follows a unified output design—storing complete pipeline results in a single JSON file (`<request_id>.json`)—while exporting token usage reports separately for model-wise and stage-wise analysis.

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
pip install json-repair
pip install asyncio
pip install pandas
pip install python-certifi-win32
pip install --upgrade certifi
pip install --upgrade grpcio grpcio-status cryptography

pip install openai
pip install -U google-genai
pip install anthropic
pip install xai_sdk
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
ANTHROPIC_API_KEY=XXXXX

# Deepseek API key used by the Deepseek client
DEEPSEEK_API_KEY=xxxxx

# NVIDIA API key used by NVIDIA clients
NVIDIA_API_KEY=XXXXX

# XAI API key used by Grok clients
XAI_API_KEY=xxxxx

# Meta API key used by Meta clients
META_API_KEY=XXXXX

# Mistral API key used by Mistral.ai clients
MISTRAL_API_KEY=XXXXX
```

Configure - Hardcodes:

- `hardcodes/model_manager.py`
- `hardcodes/prompt_manager.py`
- `hardcodes/system_prompt_manager.py`
- `hardcodes/test_request_id.py`

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
- **Anthropic Claude**
- **DeepSeek**
- **Nvidia**
- **xAI Grok**
- **Meta**
- **Mistral.ai**