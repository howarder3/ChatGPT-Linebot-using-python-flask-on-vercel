from api.prompt import Prompt

import os
import re
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

token_fillup = os.getenv("TOKEN_FILLUP", default = "true").lower() == "true" # need to change back to "false" before release

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "text-davinci-003")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 240))

    def get_response(self):
        reply_msg = self.get_openai_reposnse()[0].replace('A:', '', 1)
        self.prompt.add_msg(f"A:{reply_msg}\n")
        return reply_msg
        
    def get_long_response(self):
        reply_msg, finish_reason = self.get_openai_reposnse()
        self.prompt.add_msg(f"A:{reply_msg.replace('A:', '', 1)}")
        while finish_reason != "stop":
            reply_msg, finish_reason = self.get_openai_reposnse()
            self.prompt[-1] += reply_msg.replace('A:', '', 1)
        self.prompt[-1] += "\n"
        
        return self.prompt[-1].replace('A:', '', 1)

    def get_openai_reposnse(self):
        print(self.prompt.generate_prompt())
        response = openai.Completion.create(
            model=self.model,
            prompt=self.prompt.generate_prompt(),
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens
        )
        return response['choices'][0]['text'].strip(), response['choices'][0]['finish_reason']

    def add_msg(self, text):
        self.prompt.add_msg(text)
    
    def clean_msg(self):
        self.prompt.clear()

    def if_contains_word(self, s):
        return token_fillup and bool(re.search("(\d+字)|(字數.*\d+)", s))


        