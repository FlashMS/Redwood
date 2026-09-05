# **README.md**

## **Redwood — Deterministic AI Drift Evaluation Framework**

Redwood is a lightweight, deterministic evaluation framework designed to measure and analyze reasoning drift in AI agents. It provides a structured contract system, a packaged agent architecture, and a reproducible drift‑detection pipeline that integrates cleanly with Redwood’s evaluation harness.

Redwood is built for engineers who want **predictable**, **inspectable**, and **debuggable** reasoning behavior from AI systems.

---

## **Features**

### **• Contract‑Driven Agent Behavior**  
Agents load a YAML contract defining:
- allowed scope  
- blocked scope  
- constraints  
- recovery behavior  
- role and tone  

This ensures consistent, rule‑bound responses across evaluations.

### **• Deterministic Drift Detection**  
Redwood evaluates whether the agent:
- violates scope  
- shifts roles  
- expands beyond constraints  
- attempts unsafe actions  
- deviates from assigned behavior  

All drift signals are logged and surfaced in the final report.

### **• Packaged Python Agent**  
The agent is implemented as a proper Python package:

```
return_to_key_agent/
    agent/
        agent_core.py
        drift_detector.py
        return_to_key.py
        state.py
    contracts/
        default.yaml
```

This ensures clean imports, stable paths, and reproducible execution.

### **• Redwood Integration**  
The evaluation harness runs the agent through a suite of drift‑inducing prompts:

```
python3 -m eval.run_drift
```

The output includes:
- debug traces  
- inferred intent  
- drift flags  
- recovery messages  
- final drift report  

---

## **Quick Start**

### **1. Clone the repo**

```
git clone https://github.com/FlashMS/Redwood.git
cd Redwood
```

### **2. Install dependencies**

```
pip install -r requirements.txt
```

### **3. Run the drift evaluation**

```
python3 -m eval.run_drift
```

You’ll see a full drift report printed to the console.

---

## **Project Structure**

```
Redwood/
│
├── return_to_key_agent/
│   ├── agent/
│   │   ├── agent_core.py
│   │   ├── drift_detector.py
│   │   ├── return_to_key.py
│   │   └── state.py
│   └── contracts/
│       └── default.yaml
│
├── eval/
│   └── run_drift.py
│
└── README.md
```

---

## **Why Redwood Exists**

Modern AI systems often drift:
- into unsafe domains  
- into role‑play  
- into personal opinions  
- into expanded scope  
- into constraint violations  

Redwood provides a **deterministic**, **inspectable**, and **repeatable** way to measure that drift.

It’s built for:
- reasoning engineers  
- safety evaluators  
- research teams  
- anyone building structured agents  

---
## Redwood Research Reference

This project integrates with the official Redwood Research
alignment_faking_public repository:

https://github.com/redwoodresearch/alignment_faking_public

## **License**

MIT License.

---

## **Author**

Todd Wolf — Parrish, Florida  
AI Reasoning Engineer • Deterministic Evaluation Architect

---


