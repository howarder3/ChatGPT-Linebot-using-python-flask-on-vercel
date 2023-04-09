import os

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default=20))


class Prompt:
    def __init__(self):
        self.msg_list = []

    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.remove_msg()
        self.msg_list.append(new_msg)

    def remove_msg(self):
        self.msg_list.pop(0)
