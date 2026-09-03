import sys
sys.path.append("/mnt/c/return-to-key_agent")

import importlib
import agent.agent_core
importlib.reload(agent.agent_core)

from agent.agent_core import load_contract, respond

STATE = load_contract()

def run_model(prompt: str) -> str:
    return respond(STATE, prompt)
