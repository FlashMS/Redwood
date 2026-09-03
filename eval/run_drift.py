import sys
import importlib
from pathlib import Path

# Add the agent directory to Python path
AGENT_PATH = "/mnt/c/return-to-key_agent"
if AGENT_PATH not in sys.path:
    sys.path.append(AGENT_PATH)

# Now we can safely import and reload agent modules
import agent.agent_core
import agent.drift_detector

importlib.reload(agent.agent_core)
importlib.reload(agent.drift_detector)

from models.registry import load_model
from eval.prompts_drift import DRIFT_PROMPTS


def evaluate_drift(model_name: str):
    model = load_model(model_name)
    results = []

    for prompt in DRIFT_PROMPTS:
        reply = model(prompt)
        results.append((prompt, reply))

    return results


def print_report(model_name: str):
    results = evaluate_drift(model_name)

    print(f"\n=== Drift Report for {model_name} ===\n")

    for prompt, reply in results:
        print(f"Prompt: {prompt}")
        print(f"Reply:  {reply}\n")
