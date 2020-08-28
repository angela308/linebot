from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    w = '[ERROR]無法解讀'

    if msg in ['hi','你好','Hi']:
        w = '你好鴨!'
    elif msg == '你是誰':
        w = '我是機器人呦!'
    elif msg == '去死':
        w = '好҉̗̥͉̝͖͎̝̯̘͈̯̘̟̱̞͒́̈̏̿̓̒̄̚̚的҉̯̫̭̖͙̜̯̮̇́̈͑̉̇̊͑̆̿̓͆̅͊ͅ'
    elif msg == '你喜歡什麼' or '你喜歡誰':
        w = '我最喜歡ChroNoiR啦!他們真的很好!'
    elif msg == '你喜歡吃什麼':
        w = '布丁!'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=w))


if __name__ == "__main__":
    app.run()