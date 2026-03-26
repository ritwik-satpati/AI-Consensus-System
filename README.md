# AI Consensus System - V4 - Version 1.3.0

**Integrated Multi-Model Conditional, Configurable & Option-Driven Consensus Orchestration System**. 
A robust Python-based orchestration pipeline that leverages multiple LLMs to generate, refine, and peer-evaluate responses. 
The system ensures that the final output is not produced by a single model, but emerges from a structured multi-stage consensus and scoring process.

---

## 🚀 Overview

The AI Consensus System is built on the principle that multiple independent reasoning agents can collectively produce more reliable results than a single ai model.

### 📄 Detailed documentation

- **Architecture** $\Rightarrow$ [./Architecture.md](./Architecture.md)
- **Changelog** $\Rightarrow$ [./CHANGELOG.md](../CHANGELOG.md)
- **Limitations** $\Rightarrow$ [./Limitations.md](./Limitations.md)

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

## 📁 Directory Structure

```
AI-CONSENSUS-SYSTEM/
│
├── main.py                         # Entry point for execution
│
├── ai_consensus_system.py          # Integrated Multi-Model Conditional, Configurable & Option-Driven Consensus Orchestration System
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
├── Architecture.md                 # Detailed architecture
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

### Configure - Hardcodes:

- `hardcodes/model_manager.py`
- `hardcodes/prompt_manager.py`
- `hardcodes/system_prompt_manager.py`
- `hardcodes/test_request_id.py` [Optional - Testing only]
- `hardcodes/stages_manager.py`

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