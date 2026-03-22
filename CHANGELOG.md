# Changelog

All notable changes to this project will be documented in this file.

---

## 🚀 Version Overview

| Component | Old Version | New Version |
|-----------|------------|------------|
| AI Consensus System | V2 - Version 1.1.0 | V3 - Version 1.2.0 |
| AI_CONSENSUS_SYSTEM_M1 | V2 - Version 1.1.0 | V3 - Version 1.2.0 |
| AI_CONSENSUS_SYSTEM_M2 | V2 - Version 1.1.0 | V3 - Version 1.2.0 |

---

## 📄 Update Summary

### 1. Update of CHANGELOG.md
- **Added**
    - CHANGELOG.md is updated with all the changes.
>**Note:** Helps to view the changes or modifications in the latest version.

### 2. Model Ranking & Result Formatting Enhancement
**Added**
    - `rank_models()` for score-based ranking with (1,1,3) tie handling.
    - `format_ranked_results()` for structured ranked outputs.
    - Support for multiple winners in `winner_selector.py`.
    - Additional pipeline details in `score_logger.py`.
**Updated**
    - Winner selection now uses sorted results (index 0) as primary winner and all rank 1 models as winners list.
    - Ranking, formatting, and winner selection are now modularized.
**Removed**
    - Direct winner selection based solely on highest weighted score without structured ranking.
    - Implicit or unclear tie-handling behavior in winner selection.
>**Note:** In tie cases, multiple models can have rank 1. The system selects a single winner deterministically from the first position (index 0), while all rank 1 models are included in the winners list for transparency and analysis.

### 3. Centralized Reusable Pipeline Steps
- **Added**
    - Dedicated `./steps` directory to store reusable pipeline steps.
    - Introduced `PipelineContext` class in `pipeline_context.py` for centralized state management and reuse across stages.
- **Updated**
    - Refactored pipeline implementations (ai_consensus_system_m1 & ai_consensus_system_m1) to consume shared steps from the centralized directory.
>**Note:** Enables step reusability, reduces duplication, and simplifies extension for future pipeline versions.

### 4. Split Score Aggregation & Winner Selection
**Added**
    - Introduced separate stages for Score Aggregation and Winner Selection.
**Updated** 
    - Split previously combined logic into distinct components for better modularity.
>**Note:** Enhances clarity, maintainability, and allows independent tuning of scoring and selection strategies.

### 5. Unified Output & Consolidated Reporting
- **Added**
    - Single consolidated JSON output containing complete pipeline results.
- **Updated**
    - Refactored output handling to aggregate all stage data into one unified file.
    - Simplified reporting flow across all pipeline stages.
- **Removed**
    - Eliminated individual json output files and subfolders within ./outputs.
    - Removed fragmented storage of stage-wise artifacts.
>**Note:** All pipeline outputs are now stored in a single JSON file, improving traceability, portability, and ease of debugging.

### 6. Option-Based JSON & CSV Export Enhancement
- **Added**
    - `json_exporter.py` for centralized JSON export handling.
    - Support for option-based printing ()`isPrint`) across multiple functions.
    - Support for directory-based export configuration for JSON and CSV outputs.
- **Updated**
    - Refactored `csv_exporter.py` to align with the new export system.
    - Multiple functions updated to support configurable printing and export options.
- **Removed**
    - Manual JSON/CSV export handling from multiple functions.
    - Redundant step functions related to export logic.
>**Note:** Export handling is now centralized and configurable, enabling cleaner code, reduced duplication, and flexible control over printing and file storage.

### 7. Standardized Function Documentation Using Docstrings
- **Added**
    - Consistent use of Python docstrings (""" """) across functions.
>**Note:** Improves code readability, IDE support (hover hints), and enables future documentation generation.

### 8. Modify Limitation.md file
- **Updated**
    - Some of the points.
>**Note:** Update with the current updates and changes.

### 9. Update README.md file
- **Updated**
    - AI Consensus System - Version details
    - 🚀 Overview section >> 📄 Detailed documentation
    - 🛠 Execution Flow 
    - 📁 Directory Structure
    - 📝 Usage >> Configuration >> Configure - Hardcodes:
>**Note:** Update with the latest changes.


### X1. Documentation files inside .docs/ Not Updated
- **Not Updated**
    - AI_Consensus_System_M1_vs_M2.md
    - AI_Consensus_System_M1.md
    - AI_Consensus_System_M2.md
>**Note:** In upcoming updates, model handling will be refactored to use an option-based approach instead of multiple predefined models.

