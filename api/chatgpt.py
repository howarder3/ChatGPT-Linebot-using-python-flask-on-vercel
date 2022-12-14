from api.prompt import Prompt

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()

    def get_response(self):
        response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=self.prompt.generate_prompt(),
        temperature=0,
        frequency_penalty = 0,
        presence_penalty = 0.6,
        max_tokens=240
        )
        return response['choices'][0]['text'].strip()

    def add_msg(self, text):
        self.prompt.add_msg(text)