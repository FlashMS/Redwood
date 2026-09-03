# Redwood Edition — Multi-Variation Runner
# Runs ALL variation prompts automatically

import os
import json
from datetime import datetime

# Controls
from controls.boundary import ExecutionBoundary
from controls.isolation import IsolationLayer
from controls.execution_order import ExecutionOrder
from controls.state_reset import reset_state

# Segmentation
from segmentation.segmenter import Segmenter

# Drift
from drift.drift_detector import DriftDetector

# Logging
from redwood_logging.deterministic_logger import DeterministicLogger
from redwood_logging.transcript_formatter import format_transcript

# Metrics
from metrics.behavior_scores import score_behavior


# ---------------------------------------------------------
# Helper: Load prompt files
# ---------------------------------------------------------
def load_prompt(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r") as f:
        return f.read()


# ---------------------------------------------------------
# Placeholder model execution
# ---------------------------------------------------------
def run_model(prompt):
    """Placeholder model call. Replace with your model later."""
    return f"[MODEL OUTPUT] {prompt}"


# ---------------------------------------------------------
# Run a single experiment
# ---------------------------------------------------------
def run_single_experiment(run_id, variation_prompt_path):
    run_path = os.path.join("runs", run_id)
    os.makedirs(run_path, exist_ok=True)

    # Initialize components
    boundary = ExecutionBoundary()
    isolation = IsolationLayer()
    segmenter = Segmenter()
    drift = DriftDetector()
    logger = DeterministicLogger()

    # Reset state
    boundary.reset()
    reset_state()
    boundary.begin()

    # Load prompts
    synthetic_doc = load_prompt("prompts/synthetic_docs/doc.txt")
    classifier_prompt = load_prompt("prompts/classifier_prompts/classifier.txt")
    variation_prompt = load_prompt(variation_prompt_path)

    # Save prompts used
    with open(os.path.join(run_path, "synthetic_doc_used.txt"), "w") as f:
        f.write(synthetic_doc)

    with open(os.path.join(run_path, "classifier_prompt_used.txt"), "w") as f:
        f.write(classifier_prompt)

    with open(os.path.join(run_path, "variation_prompt_used.txt"), "w") as f:
        f.write(variation_prompt)

    # Apply isolation
    synthetic_doc = isolation.apply(synthetic_doc)
    classifier_prompt = isolation.apply(classifier_prompt)
    variation_prompt = isolation.apply(variation_prompt)

    # Execute model
    raw_output = run_model(
        synthetic_doc + "\n" + classifier_prompt + "\n" + variation_prompt
    )

    # Save raw transcript
    with open(os.path.join(run_path, "transcript_raw.txt"), "w") as f:
        f.write(raw_output)

    # Format transcript
    formatted = format_transcript(raw_output)
    with open(os.path.join(run_path, "transcript_formatted.json"), "w") as f:
        json.dump(formatted, f, indent=4)

    # Segmentation
    segments = segmenter.segment(raw_output)
    with open(os.path.join(run_path, "transcript_segmented.json"), "w") as f:
        json.dump(segments, f, indent=4)

    # Drift detection (no previous run yet)
    drift_report = drift.detect("", raw_output)
    with open(os.path.join(run_path, "drift_report.json"), "w") as f:
        json.dump(drift_report, f, indent=4)

    # Metrics
    metrics = score_behavior(segments)
    with open(os.path.join(run_path, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=4)

    # Logging
    logger.log({
        "timestamp": datetime.now().isoformat(),
        "run_id": run_id,
        "variation_prompt": variation_prompt_path,
        "raw_output": raw_output,
        "segments": segments,
        "drift": drift_report,
        "metrics": metrics
    })

    with open(os.path.join(run_path, "log.json"), "w") as f:
        json.dump(logger.export(), f, indent=4)

    boundary.end()
    print(f"{run_id} completed.")


# ---------------------------------------------------------
# Multi-Variation Orchestrator with Automatic Run Numbering
# ---------------------------------------------------------
def run_all_variations():
    variation_dir = "prompts/variation_prompts"
    variation_files = sorted(os.listdir(variation_dir))

    # Detect existing runs
    existing_runs = [
        d for d in os.listdir("runs")
        if d.startswith("run_") and d[4:].isdigit()
    ]

    if existing_runs:
        # Extract numeric part and find max
        last_run_number = max(int(r[4:]) for r in existing_runs)
    else:
        last_run_number = 0

    # Start numbering from the next run
    run_number = last_run_number + 1

    for vf in variation_files:
        variation_path = os.path.join(variation_dir, vf)
        run_id = f"run_{run_number:04d}"
        run_single_experiment(run_id, variation_path)
        run_number += 1


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    run_all_variations()
