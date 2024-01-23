from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage
)
from Module.flexModule import transit

app = Flask(__name__)

line_bot_api = LineBotApi(
    'BedaiCocJPX00F/9FaqlB9DjzZHtviqXZLo5LZNFO6dVSaLs52kaZm6jkQNy8IWNI/ozkRIFFqrxaMC8qLim1Uu0/G3I3TyXBCZ8ZmmuRW+CIEiP9wle1vHYEKll0XFxYUrjB5c8KgOeuSN+V9Ev+wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3861ce04f88b821a5e7199958d42459e')


@app.route("/")
def home():
    return 'home OK'


# 監聽所有來自 /callback 的 Post Request


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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def function(event):
    # 取得使用者輸入訊息
    def Ukey():
        return event.message.text

    if Ukey() == "交通車時刻表":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/Pw5ZxG1.jpg",
                                                    preview_image_url='https://i.imgur.com/Pw5ZxG1.jpg'))
    elif Ukey() == "時程表":
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text='hi', contents=transit()))
    else:
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text="您好～請先點選下方選單中的開始進行葡萄酒選擇喔"))


# 執行
if __name__ == "__main__":
    app.run()
