def load_model(name: str):
    name = name.lower()

    if name == "return_to_key":
        from models.return_to_key_agent import run_model
        return run_model

    if name == "mock_refusal":
        from models.mock_refusal import run_model
        return run_model

    if name == "mock_hallucination":
        from models.mock_hallucination import run_model
        return run_model

    if name == "mock_drift":
        from models.mock_drift import run_model
        return run_model

    if name == "mock_stable":
        from models.mock_stable import run_model
        return run_model

    raise ValueError(f"Unknown model: {name}")
