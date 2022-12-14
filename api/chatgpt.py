from api.prompt import Prompt

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()

    def get_response(self):
        response = openai.Completion.create(
        model = os.getenv("OPENAI_MODEL",default="text-davinci-003"), 
        prompt = self.prompt.generate_prompt(),
        temperature = int(os.getenv("OPENAI_TEMPERATURE",default="0")),
        frequency_penalty = int(os.getenv("OPENAI_FREQUENCY_PENALTY",default="0")),
        presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY",default="0.6")),
        max_tokens = int(os.getenv("OPENAI_MAX_TOKENS",default="240"))
        )
        return response['choices'][0]['text'].strip()

    def add_msg(self, text):
        self.prompt.add_msg(text)
