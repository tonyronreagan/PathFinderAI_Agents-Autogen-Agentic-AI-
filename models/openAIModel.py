from config.settings import MODEL, OPENAI_API_KEY, DEEPSEEK_V3_API_KEY
from autogen_ext.models.openai import OpenAIChatCompletionClient
from openai import OpenAI

model_client1 = OpenAIChatCompletionClient(
    model=MODEL,
    openai_api_key=OPENAI_API_KEY,
)


model_client = OpenAIChatCompletionClient(
    model=MODEL,
    openai_api_key=DEEPSEEK_V3_API_KEY,
)
