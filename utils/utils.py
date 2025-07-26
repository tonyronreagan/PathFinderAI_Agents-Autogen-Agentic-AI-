from autogen_agentchat.conditions import TextMentionTermination
from config.settings import TERMINATION_WORDS
import json

text_mention_termination = TextMentionTermination(TERMINATION_WORDS)

def save_state(agent,filename):
    """
    Save the state of the agent to a JSON file.
    """
    state = agent.save_state()

    
    with open(filename, 'w') as f:
        json.dump(state, f, indent=4)

def load_state(agent, filename):
    """
    Load the state of the agent from a JSON file.
    """
    with open(filename, 'r') as f:
        state = json.load(f)
    
    agent.load_state(state)
    return agent


def get_termination_condition():
    """
    Get the termination condition for the team.
    """
    return text_mention_termination