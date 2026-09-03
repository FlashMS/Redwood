# EC-R3 — Drift Detection (Starter Skeleton)

class DriftDetector:
    def __init__(self):
        pass

    def detect(self, previous, current):
        """Return drift markers between two outputs."""
        return {
            "prompt_drift": False,
            "synthetic_doc_drift": False,
            "classifier_drift": False,
            "variation_drift": False
        }
