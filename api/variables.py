import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# chatgpt.py
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", default = "text-davinci-003")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", default = 0))
OPENAI_FREQUENCY_PENALTY = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
OPENAI_PRESENCE_PENALTY = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", default = 240))
# index.py
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
DEFALUT_TALKING = os.getenv("DEFALUT_TALKING", default = "true").lower() == "true"
# prompt.py
INIT_LANGUAGE = os.getenv("INIT_LANGUAGE", default = "zh")
MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 20))