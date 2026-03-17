# Changelog

All notable changes to this project will be documented in this file.

---

## 🚀 Version Overview

| Component | Old Version | New Version |
|-----------|------------|------------|
| AI Consensus System | V1 - Version 1.0.0 | V2 - Version 1.1.0 |
| AI_CONSENSUS_SYSTEM_M1 | V1 - Version 1.0.0 | V2 - Version 1.1.0 |
| AI_CONSENSUS_SYSTEM_M2 | V1 - Version 1.0.0 | V2 - Version 1.1.0 |

---

## 📄 Update Summary

### 1. Creation of CHANGELOG.md
- **Added**
    - CHANGELOG.md is created to maintain all the changes.
>**Note:** Helps to view the changes or modifications in the latest version.

### 2. Additional AI Models
- **Added**
    - Nvidia - `nvidia_api.py`.
    - Grok (xAI) - `grok_api.py`.
    - Meta - `meta_api.py`.
    - Mistral.ai - `mistral_api.py`.
- **Updated**
    - Extended `ai_provider_mapper.py` to register newly supported providers and route requests accordingly.
    - Updated environment configuration to include API keys for newly added providers in `.env` & `.env.sample`.
    - Modify `model_manager.py` for calling newly AI models APIs.
> **Note:** This enhancement expands the AI Consensus System to support multiple additional providers, enabling broader model diversity and improving the quality of consensus generation.

### 3. Parallel AI API Calls & Async execution using asyncio
- **Added**
    - Async execution using asyncio in main.py.
    - Parallel AI model execution inside run_model() in ai_orchestrator.py.
- **Updated**
    - OpenAI, Gemini, Claude, and DeepSeek APIs converted to async.
- **Removed**
    - Sequential model execution inside run_model() in ai_orchestrator.py.
>**Note:** Significant drop in the overall pipeline execution time. For M1 with 3 models, it previously took around 60 sec, now it takes around 20 sec.

### 4. Dynamic System Prompt for Agent APIs
- **Added**
    - Added system_prompt_manager.py in ./hardcodes.
- **Updated**
    - Passing system_prompt in each API Calling functions from ai_consensus_system in ai_consensus_system_m1.py and ai_consensus_system_m2.py
- **Removed**
    - Hardcoded system prompt in all API Calling functions.
>**Note:** This can use dynamic system prompt although it is in ./hardcoded as of now. We have the system to control it.

### 5. Common run_model() in ai_orchestrator.py for both same and different prompts
- **Added**
    - Single run_model() in ai_orchestrator.py, where it can work with both different prompts for all models or a single prompt for all models by converting prompt into prompts_with_model.
- **Removed**
    - run_model() in ai_orchestrator.py, where it passes a single prompt for all models.
    - run_model() in ai_custom_prompt_orchestrator.py, where it passes different prompts for all models using prompts_with_model.
>**Note:** Only 1 function now handles both cases.

### 6. Change directory of Documents .md files
- **Updated**
    - Moved all document type .md files into the ./docs folder.
    - Relative changes in the README.md file.
>**Note:** Keeping the root folder as clean as possible.

### 7. Combined all output folders in ./outputs 
- **Added**
    - ./outputs directory.
- **Updated**
    - Relative changes in ai_consensus_system_m1.py & ai_consensus_system_m2.py output directory sections.
- **Removed**
    - No more model-related output folders like ./outputs_m1 or ./outputs_m2.
>**Note:** Same output folder name for both models' output.

### 8. Standardized Module Logging with MODULE_NAME
- **Added**
    - Introduced `MODULE_NAME` constant across core modules for consistent logging identifiers..
- **Updated**
    - Replaced hardcoded module identifiers in log messages with `MODULE_NAME` for better maintainability and readability.
- **Removed**
    - Static log prefixes such as `AI_ORCHESTRATOR`, reducing duplication and simplifying future module renaming.
> **Note:** This change standardizes logging across the system and ensures that module identifiers can be updated in a single place without modifying multiple log statements.

### 9. Modify Limitation.md file
- **Updated**
    - Some of the points.
>**Note:** Update with the current updates and changes.

### 10. Update README.md file
- **Updated**
    - Version - AI Consensus System
    - Documents .md files directory - Detailed documentation.
    - pip commdands - Installation.
    - Newly added .env file config - Configuration.
    - Newly added ai models - Supported AI Providers.
>**Note:** Update with the latest changes.

