import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPSEEK_V3_API_KEY = os.getenv("DEEPSEEK_V3_API_KEY")
MODEL = 'gpt-4o-mini'
MAX_TURNS = 5
MAX_TURNS_10 = 10


TERMINATION_WORDS = ['stop', 'end', 'quit', 'exit']

