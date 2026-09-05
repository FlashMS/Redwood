import sys
import importlib
from pathlib import Path

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
if __name__ == "__main__":
    print_report("return_to_key")
