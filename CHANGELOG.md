# Changelog

All notable changes to this project will be documented in this file.

---

## 🚀 Version Overview

| Component | Old Version | New Version |
|-----------|------------|------------|
| AI Consensus System | V3 - Version 1.2.0 | V4 - Version 1.3.0 |

---

## 📄 Update Summary

### 1. Update of CHANGELOG.md
- **Added**
    - New changes in Update Summary.
- **Updated**
    - Versions of `AI Consensus System` in Version Overview.
- **Removed**
    - `AI Consensus System M1` & `AI Consensus System M2` in Version Overview.
    - Previous all updates in Update Summary.
>**Note:** Helps to view the changes or modifications in the latest version.

### 2. Integrated both M1 & M2 Models into Single Orchestration Model
- **Added**
    - Unified pipeline entry point `run_ai_consensus_system()` to orchestrate full execution flow in `ai_consensus_system.py`.
    - Introduced conditional stage execution using `evaluation_stage` and `scoring_stage` via `PipelineContext`.
    - Added optional execution of `CONSENSUS_SYNTHESIS` for cost optimization, controlled through `evaluation_stage`.
    - Enabled conditional selection of scoring strategies via `scoring_stage`: `SCORING_COMBINED` & `SCORING_RANDOM`
- **Updated**
    - Pipeline flow refactored into a single orchestrator replacing separate M1 and M2 flows in `main.py`
- **Removed**
    - AI Consensus System M1 Model pipeline - `ai_consensus_system_m1.py`
    - AI Consensus System M2 Model pipeline - `ai_consensus_system_m2.py`
>**Note:** The system is now fully configuration-driven. Consensus Synthesis always includes Initial Execution, while scoring behavior is dynamically selected between accuracy-focused (combined) and cost-optimized (random) strategies using runtime flags. The pipeline now supports 4 different execution modes by combining evaluation and scoring conditions and options.

### 3. Added Stages Handler
- **Added**
    - Introduced `stages_manager.py` in hardcodes for centralized stage control (currently update/modify-only configuration layer).
    - Created `stage_validator.py` for stage validation and dependency support.
>**Note:** Improves stage reusability, reduces duplication, and simplifies extension for future pipeline versions.

### 4. Architecture.md Introduced
**Added**
    - Detailed architecture documentation for the Integrated Multi-Model Consensus Pipeline in `Architecture.md`.
>**Note:** Provides a clear and structured understanding of the system design, execution flow, and configuration-driven behavior.

### 5. Documentation files inside .docs/ Revomed 
- **Removed**
    - Deleted ./docs folder supporting M1 & M2 file : `AI_Consensus_System_M1.md`, `AI_Consensus_System_M2.md` & `AI_Consensus_System_M1_vs_M2.md`
>**Note:** Documents are not needed any more after removed M1 & M2 models. 

### 6. Modify Limitation.md file
- **Updated**
    - Some of the points.
>**Note:** Update with the current updates and changes.

### 7. Update README.md file
- **Added**
    - `Architecture`, `Changelog` & `Limitations` in Detailed documentation
- **Updated**
    - AI Consensus System - Version details
    - 🚀 Overview section >> 📄 Detailed documentation
    - 📁 Directory Structure
    - 📝 Usage >> Configuration >> Configure - Hardcodes:
- **Removed**
    - `AI Consensus System – M1 Architecture`, `AI Consensus System – M2 Architecture` & `M1 vs M2 Comparison`
    - 🛠 Execution Flow (Common to M1 & M2)
>**Note:** Update with the latest changes.