from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, msg, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('/0xbdUu4bS3SCY3+P5gd+4rj9CYHBaBfejoXsAy0Bc4/D55ScaGtTxRf+YNwY5SpflXY41UwSMKdrT2RLiIGJFupyCpSISO/TJ0Uv1yYSfkLczxJBFVx3EcXWQzMm8mN3bIVmgPikBr+yKz64HwaGQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2e70c2c3a05171027dc2b81f4879496b')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=msg)
def handle_message(event):
    msg = event.message.text
    word = '抱歉...我聽不懂...還在開發中'
    if msg == '你好' or 'hi':
        word = '你好!!!'
    elif msg == '你是誰?':
        word = '我是機器人喔!'
    else
        sticker_message = StickerSendMessage(
            package_id='2',
            sticker_id='23'
        )
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=word))


if __name__ == "__main__"
    app.run()