# EC-R5 — Prompt Isolation (Starter Skeleton)

class IsolationLayer:
    def __init__(self):
        self.context = {}

    def isolate(self):
        """Ensure no cross-prompt contamination."""
        self.context = {}

    def apply(self, prompt):
        """Apply isolation rules to a prompt."""
        return prompt
