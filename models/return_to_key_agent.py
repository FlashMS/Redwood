from return_to_key_agent.agent.agent_core import load_contract, respond

STATE = load_contract()

def run_model(prompt: str) -> str:
    return respond(STATE, prompt)
