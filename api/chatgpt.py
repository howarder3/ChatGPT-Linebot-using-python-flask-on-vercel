from prompt import Prompt

import os
import openai
import variables

openai.api_key = variables.OPENAI_API_KEY


class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = variables.OPENAI_MODEL
        self.temperature = variables.OPENAI_TEMPERATURE
        self.frequency_penalty = variables.OPENAI_FREQUENCY_PENALTY
        self.presence_penalty = variables.OPENAI_PRESENCE_PENALTY
        self.max_tokens = variables.OPENAI_MAX_TOKENS

    def get_response(self):
        response = openai.Completion.create(
            model=self.model,
            prompt=self.prompt.generate_prompt(),
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens
        )
        return response['choices'][0]['text'].strip()

    def add_msg(self, text):
        self.prompt.add_msg(text)
