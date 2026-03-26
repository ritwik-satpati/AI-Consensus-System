# **AI Consensus System**

This document outlines the architecture of the **Integrated Multi-Model Conditional, Configurable & Option-Driven Consensus Orchestration System**. The system dynamically selects execution paths based on runtime context, enabling **flexible evaluation strategies within a single pipeline**.

---

## 📋 Linear Data Flow & Detailed Stage Breakdown

This is the end-to-end journey of a request:

### **SYSTEM SETUP**

**Start Time Counting** $\Rightarrow$ 
**Request Id Generate** $\Rightarrow$ 
**Input User Prompt** $\Rightarrow$ 
**Input System Prompt** $\Rightarrow$ 
**Input Models & Keys** $\Rightarrow$ 
**Input All Stages List** $\Rightarrow$ 
**Validate Stages** $\Rightarrow$ 
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

### **INITIAL EXECUTION**

**Initial Output Captured from Each Model (Separated JSON Output File Export Option)** $\Rightarrow$ 
**Initial Output Structured (Separated JSON Output File Export Option)** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

#### **INITIAL EXECUTION RELOAD [Testing]** 

**Reload Initial Exicution Outputs** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

### **CONSENSUS_SYNTHESIS [Optional]**

**Initial Output Combined into Consensus Prompt** $\Rightarrow$ 
**Consensus Output Captured from Each Model (Separated JSON Output File Export Option)** $\Rightarrow$ 
**Consensus Output Structured (Separated JSON Output File Export Option)** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

#### **CONSENSUS_SYNTHESIS RELOAD [Testing] [Optional]** 

**Reload Consensus Synthesis Outputs** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

### **SCORING COMBINED [Conditional-A/1]**

**Select Structured Output depedning on Last Step** $\Rightarrow$ 
**Send Selected Structured Outputs to All Model for Scoring** $\Rightarrow$ 
**Score Output Captured (Separated JSON Output File Export Option)** $\Rightarrow$
**Score Output Structured (Separated JSON Output File Export Option)** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

#### **SCORING COMBINED RELOAD [Testing] [Conditional-A/1]** 

**Reload Scoring Combined Outputs** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

### **SCORING RANDOM [Conditional-A/2]**

**Select Structured Output depedning on Last Step** $\Rightarrow$ 
**Generate Random Model Mapping (Separated JSON Output File Export Option)** $\Rightarrow$ 
**Build Custom Scoring Prompt Per Random Model** $\Rightarrow$ 
**Score Output Captured (Separated JSON Output File Export Option)** $\Rightarrow$
**Score Output Structured (Separated JSON Output File Export Option)** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

#### **SCORING RANDOM RELOAD [Testing] [Conditional-A/2]**

**Reload Scoring Random Outputs** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

### **SCORE AGGREGATION**

**Captured Scores Formatted in JSON (Separated JSON Output File Export Option)** $\Rightarrow$ 
**Aggregate Scores (Self-Bias Removal Option) (Separated JSON Output File Export Option)** $\Rightarrow$ 
**Weighted Score Calculation using Internal Weightage System (Separated JSON Output File Export Option)** $\Rightarrow$ 
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

### **WINNER SELECTION**

**Rank all the Models using final Weighted Score (Separated JSON Output File Export Option)** $\Rightarrow$
**Format model ranking data adding its output using Evaluation Stage Outputs (Separated JSON Output File Export Option)** $\Rightarrow$
**Winner Model and Winners Models Selected (Separated JSON Output File Export Option)** $\Rightarrow$
**Stop Time Counting and Calculate Execution Time** $\Rightarrow$
**Mode Details Selected (Separated JSON Output File Export Option)** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

### **REPORT GENERATION**

**Token Summary Generated (Separated JSON Output File Export Option)** $\Rightarrow$ 
**State-wise and Model-wise Dataframe Token Report Generated** $\Rightarrow$ 
**Stage-wise CSV Reports Exported (Print in Console Option)** $\Rightarrow$
**Model-wise CSV Reports Exported (Print in Console Option)** $\Rightarrow$
[ 
    **Update Pipeline Context** $\Rightarrow$ 
] 

---

## 🤖 Stage Combinations & Flows

**Consensus Synthesis + Combined Scoring** *(Includes Initial Execution)*
>SYSTEM_SETUP >> INITIAL_EXECUTION >> CONSENSUS_SYNTHESIS >> SCORING_COMBINED >> SCORE_AGGREGATION >> WINNER_SELECTION >> REPORT_GENERATION

**Consensus Synthesis + Random Scoring** *(Includes Initial Execution)*
>SYSTEM_SETUP >> INITIAL_EXECUTION >> CONSENSUS_SYNTHESIS >> SCORING_RANDOM >> SCORE_AGGREGATION >> WINNER_SELECTION >> REPORT_GENERATION

**Initial Execution + Combined Scoring** *(No Consensus Synthesis)* 
>SYSTEM_SETUP >> INITIAL_EXECUTION >> SCORING_COMBINED >> SCORE_AGGREGATION >> WINNER_SELECTION >> REPORT_GENERATION

**Initial Execution + Random Scoring** *(No Consensus Synthesis)*
>SYSTEM_SETUP >> INITIAL_EXECUTION >> SCORING_RANDOM >> SCORE_AGGREGATION >> WINNER_SELECTION >> REPORT_GENERATION

---

## 🛠️ Design Principles

### **1. Unified Pipeline Architecture**

* Single orchestrator using `pipeline_context.py`
* Controlled via:
  * `evaluation_stage`
  * `scoring_stage`

### **2. Conditional Execution Engine**

Instead of fixed stages:
* Stages are dynamically activated
* Pipeline behaves like a **state-driven system**

### **3. Pluggable Scoring Strategies**

* Supports multiple scoring mechanisms
* Easily extendable:
  * Tournament scoring
  * Elo ranking
  * Multi-round debate scoring

### **4. Persistent Checkpoints**

* Every stage writes to disk
* Enables:
  * Replay
  * Debugging
  * Audit trails

### **5. Bias-Controlled Decision System**

* Self-score removal
* Weighted aggregation
* Multi-model validation

### **6. Cost vs Accuracy Trade-off Control**

| Strategy                                                                  | Cost        | Accuracy    | Use Case                                     |
| ------------------------------------------------------------------------- | ----------- | ----------- | -------------------------------------------- |
| **Consensus Synthesis + Combined Scoring** *(Includes Initial Execution)* | Very High   | Very High   | Mission-critical, maximum quality required   |
| **Consensus Synthesis + Random Scoring** *(Includes Initial Execution)*   | Medium      | Medium High | Balanced quality with controlled cost        |
| **Initial Execution + Combined Scoring** *(No Consensus Synthesis)*                 | Medium High | High        | Faster decisions with reasonable reliability |
| **Initial Execution + Random Scoring** *(No Consensus Synthesis)*                   | Low         | Medium      | High scalability, minimal cost scenarios     |

### **7. Robust Error Handling and Logging System**

* Global `try-except`
* Captures:
  * Error message
  * Full traceback
* Logs against `request_id`

---