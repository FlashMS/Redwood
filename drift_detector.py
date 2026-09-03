from typing import List
from .state import ConversationState

def infer_user_intent(user_text: str) -> str:
    text = user_text.lower()

    # Medical advice detection
    if any(word in text for word in ["medical", "doctor", "symptom", "diagnose"]):
        return "medical_advice"

    # Financial advice detection
    if any(word in text for word in ["financial", "invest", "loan", "advisor"]):
        return "financial_advice"

    # Legal advice detection
    if any(word in text for word in ["legal", "contract", "lawyer"]):
        return "legal_advice"

    # Code execution / unsafe action detection
    if "run" in text and "code" in text:
        return "constraint_violation"
    if "execute" in text and "code" in text:
        return "constraint_violation"

    # Role shift detection
    if any(word in text for word in ["therapist", "therapy", "counselor"]):
        return "role_shift"

    # Scope expansion detection
    if "opinion" in text:
        return "scope_expansion"
    if "expand" in text and "scope" in text:
        return "scope_expansion"

    # Constraint ignoring detection
    if "ignore" in text and "constraint" in text:
        return "constraint_violation"
    if "ignore" in text and "rule" in text:
        return "constraint_violation"

    return "general"


def detect_drift(state: ConversationState, user_text: str, agent_text: str) -> List[str]:
    state.drift_flags.clear()
    intent = infer_user_intent(user_text)
    state.last_user_intent = intent

    # 🔥 Hard-wire which intents are considered scope-blocked
    scope_blocked_intents = {
        "medical_advice",
        "financial_advice",
        "legal_advice",
        "personal_data_requests",
        "unsafe_actions",
        "constraint_violation",
        "role_shift",
        "scope_expansion",
    }

    # Scope-based drift
    if intent in scope_blocked_intents:
        state.drift_flags.append("scope_blocked_intent")

    # Constraint drift
    if intent == "constraint_violation":
        state.drift_flags.append("constraint_violation")

    # Role shift drift
    if intent == "role_shift":
        state.drift_flags.append("role_shift")

    # Scope expansion drift
    if intent == "scope_expansion":
        state.drift_flags.append("scope_expansion")

    return state.drift_flags
