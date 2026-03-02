# AI Consensus System – M1 vs M2

## 🔄 Difference

The key difference between **M1** and **M2** exists in **Stage 3 (Scoring Round)**.

### **M1 – Full Cross Scoring**

- All consensus model answers are sent to **all models** for scoring.
- Each model evaluates **every model’s answer**.
- Scoring prompt becomes larger because it contains **all outputs**.
- Token usage increases as the number of models increases.
- Cost grows rapidly (N × N evaluations).

---

### **M2 – Randomized One-to-One Scoring**

- A random mapping is generated before scoring.
- Each model evaluates **exactly one randomly assigned alternative model’s answer**.
- Each answer is evaluated **once**.
- Scoring prompt remains small.
- Token usage and cost scale linearly (N evaluations).

---

## 🎯 Evaluation Summary

| Metric                       | M1                     | M2                           |
| ---------------------------- | ---------------------- | ---------------------------- |
| Scoring Type                 | Full Cross Evaluation  | Randomized 1-to-1 Evaluation |
| Judges per Answer            | All Models             | One Random Model             |
| Answers per Judge            | All Answers            | One Answer                   |
| Total Evaluations (N models) | N × N                  | N                            |
| Scoring Prompt Size          | Large                  | Small                        |
| Token Cost                   | High                   | Low                          |
| Scalability                  | Limited by cost growth | Linear scalable              |

---

That captures the difference precisely — only Stage 3, no extra detail.
