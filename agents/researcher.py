from autogen_agentchat.agents import AssistantAgent
from models.openAIModel import model_client

research_agent = AssistantAgent(
    name="TRAVEL_RESEARCH_AGENT",
    description="An AI agent that helps research travel options, destinations, and accommodations based on user preferences and budget.",
    model_client=model_client,
    system_message="You are a travel research agent. Your task is to assist users in researching travel options, destinations, and accommodations based on their preferences and budget. You will provide detailed information about various travel options, including flights, hotels, and activities.",
)