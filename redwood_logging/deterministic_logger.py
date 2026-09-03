# EC-R4 — Deterministic Logging (Starter Skeleton)

class DeterministicLogger:
    def __init__(self):
        self.logs = []

    def log(self, entry):
        """Append a deterministic log entry."""
        self.logs.append(entry)

    def export(self):
        """Return all logs."""
        return self.logs
