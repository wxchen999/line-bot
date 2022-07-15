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

line_bot_api = LineBotApi('Gn2EgnijiWD5aXA4AFOr8BaHxZTm+quOm/+PrsbeTptcMYUgRk4ezGaRMg/jwORnPHW42Mc2Ma86YY4n5oJvSK2Aq57yGmSfbHn0yHGCPsRbKudEkUCHIuxPj9WX1QTz2YUaSdJsTHN2bZ0y7cmcDwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bc0fab5f57f5f0df2d7f2bda82844f9f')


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
    r =  '看不懂你在說啥'
    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()