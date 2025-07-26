from autogen_agentchat.agents import AssistantAgent
from models.openAIModel import model_client

planner_agent = AssistantAgent(
    name="TRAVEL_PLANNER_AGENT",
    description="An AI agent that helps plan travel itineraries and help users find the best travel options based on their preferences and budget.",
    model_client = model_client,
    system_message="You are a travel planner agent. Your task is to assist users in planning their travel itineraries, finding the best travel options based on their preferences and budget, and providing recommendations for destinations, accommodations, and activities.",
)