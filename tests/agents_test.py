import pytest
from agents.planner import planner_agent

def test_planner_agent():
    """
    Test the planner agent's initialization and attributes.
    """
    assert planner_agent.name == "TRAVEL_PLANNER_AGENT"
    assert planner_agent.description == "An AI agent that helps plan travel itineraries and help users find the best travel options based on their preferences and budget."
    assert planner_agent.model is not None
    assert planner_agent.system_message == "You are a travel planner agent. Your task is to assist users in planning their travel itineraries, finding the best travel options based on their preferences and budget, and providing recommendations for destinations, accommodations, and activities."

test_planner_agent()