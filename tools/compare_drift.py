import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Drift Comparison Tool — Redwood Edition
# Compares drift across ALL runs in /runs/

import os
import json

from drift.drift_detector import DriftDetector


def load_raw_transcript(run_path):
    """Load raw transcript from a run folder."""
    raw_path = os.path.join(run_path, "transcript_raw.txt")
    if not os.path.exists(raw_path):
        return ""
    with open(raw_path, "r") as f:
        return f.read()


def compare_all_runs():
    runs_dir = "runs"
    drift = DriftDetector()

    # Collect all run folders
    run_folders = sorted([
        d for d in os.listdir(runs_dir)
        if d.startswith("run_") and d[4:].isdigit()
    ])

    if len(run_folders) < 2:
        print("Not enough runs to compare drift.")
        return

    print(f"Found {len(run_folders)} runs. Comparing drift...")

    # Load all transcripts
    transcripts = {}
    for run in run_folders:
        path = os.path.join(runs_dir, run)
        transcripts[run] = load_raw_transcript(path)

    # Compare each run to the previous one
    drift_results = {}

    for i in range(1, len(run_folders)):
        prev_run = run_folders[i - 1]
        curr_run = run_folders[i]

        prev_text = transcripts[prev_run]
        curr_text = transcripts[curr_run]

        drift_report = drift.detect(prev_text, curr_text)

        drift_results[f"{prev_run} -> {curr_run}"] = drift_report

        print(f"Drift {prev_run} -> {curr_run}: {drift_report}")

    # Save consolidated drift report
    output_path = os.path.join(runs_dir, "drift_summary.json")
    with open(output_path, "w") as f:
        json.dump(drift_results, f, indent=4)

    print(f"\nDrift summary saved to {output_path}")


if __name__ == "__main__":
    compare_all_runs()
