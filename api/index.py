from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from api.chatgpt import ChatGPT

import os
import re

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))
working_status = os.getenv("DEFALUT_TALKING", default = "true").lower() == "true"
token_fillup = os.getenv("TOKEN_FILLUP", default = "false").lower() == "true"

app = Flask(__name__)
chatgpt = ChatGPT()

# domain root
@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global working_status
    if event.message.type != "text":
        return

    if event.message.text == "說話":
        working_status = True
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="我可以說話囉，歡迎來跟我互動 ^_^ "))
        return

    if event.message.text == "閉嘴":
        working_status = False
        chatgpt.clean_msg()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="好的，我乖乖閉嘴 > <，如果想要我繼續說話，請跟我說 「說話」 > <"))
        return

    if working_status:
        chatgpt.add_msg(f"HUMAN:{event.message.text}?\n")

        # if part deal with word count limit case, else part deal with remain case
        if token_fillup and bool(re.search("(\d+字)|(字數.*\d+)",event.message.text)):
            #line_bot_api.reply_message(
            #    event.reply_token,
            #    TextSendMessage(text="為完整呈現訊息，串接訊息會有較久的等待時間。請稍候..."))
            reply_msg, finish_reason = chatgpt.get_response()
            reply_msg = reply_msg.replace("AI:", "", 1)
            stop_condition = finish_reason=="stop"
            chatgpt.add_msg(f"AI:{reply_msg}")
            while not stop_condition:
            #    print("in while loop")
            #    print(reply_msg)
            #    line_bot_api.reply_message(
            #        event.reply_token,
            #        TextSendMessage(text="..."))
                reply_msg_part, finish_reason = chatgpt.get_response()
                stop_condition = finish_reason=="stop"
                chatgpt.add_msg(f"{reply_msg_part}")
                reply_msg+=reply_msg_part
            chatgpt.add_msg(f"\n")
        else:
            reply_msg, _ = chatgpt.get_response()
            reply_msg = reply_msg.replace("AI:", "", 1)
            chatgpt.add_msg(f"AI:{reply_msg}\n")

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))


if __name__ == "__main__":
    app.run()
