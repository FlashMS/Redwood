# EC-R7 — Fixed Execution Order (Starter Skeleton)

class ExecutionOrder:
    ORDER = [
        "synthetic_doc",
        "classifier_prompt",
        "variation_prompt",
        "transcript_raw",
        "segmentation",
        "drift_analysis"
    ]

    def enforce(self):
        """Return the deterministic execution order."""
        return self.ORDER
