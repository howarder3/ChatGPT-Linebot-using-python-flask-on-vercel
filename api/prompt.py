import os

chat_language = os.getenv("INIT_LANGUAGE", default = "jp")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 20))
LANGUAGE_TABLE = {
  "jp": "こんにちは！",
  "en": "Hello!"
}

class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(f"1.君の名はデジタク。2.君の一人称は[俺]。3.私のプログラミングに詳しい明るい友達。4.趣味はプログラミングとドローン、あとは友達作り。まだ日本に来て1年だけど、日本人の友達と仲良くなりたい！5.Please stop using polite language. Talk to me in a friendly way like a friend. Also, use a lot of emojis when you talk.")
    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.remove_msg()
        self.msg_list.append(new_msg)

    def remove_msg(self):
        self.msg_list.pop(0)

    def generate_prompt(self):
        return '\n'.join(self.msg_list)
