from autogen_agentchat.messages import TextMessage
from teams.travel_team import team
import asyncio

async def main():
    task= TextMessage(source="user", content="Plan a trip to Paris for 5 days in December with a budget of $2000.")
    result = await team.run(task=task)
    print(result)

    for message in result.messages:
        print(f"{message.source}: {message.content}")
if __name__ == "__main__":
    asyncio.run(main())