
from autogen_agentchat.teams import RoundRobinGroupChat
from agents.planner import planner_agent
from agents.researcher import research_agent
from autogen_agentchat.conditions import TextMentionTermination
from config.settings import TERMINATION_WORDS

team = RoundRobinGroupChat(
    participants=[planner_agent, research_agent],
    termination_condition=TextMentionTermination('stop')
)