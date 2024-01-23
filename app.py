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


contents = {
    "type": "bubble",
    "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "FROM",
                "offsetStart": "10px",
                "offsetTop": "5px",
                "color": "#9D9D9D",
                "weight": "bold"
            },
            {
                "type": "text",
                "text": "Taoyuan",
                "offsetTop": "5px",
                "offsetStart": "20px",
                "size": "30px"
            },
            {
                "type": "text",
                "text": "TO",
                "offsetTop": "5px",
                "offsetStart": "10px",
                "color": "#9D9D9D",
                "weight": "bold"
            },
            {
                "type": "text",
                "text": "Chayi",
                "offsetTop": "5px",
                "offsetStart": "20px",
                "size": "30px"
            },
            {
                "type": "separator"
            }
        ],
        "spacing": "5px",
        "backgroundColor": "#D8D8EB",
        "alignItems": "flex-start"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "時程表",
                        "size": "25px",
                        "weight": "bold"
                    }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "text",
                                "text": "第一站"
                            },
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                "offsetEnd": "20px"
                            },
                            {
                                "type": "text",
                                "text": "07:00"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://i.imgur.com/VNeqIZ2.png",
                                "offsetStart": "45px"
                            },
                            {
                                "type": "text",
                                "text": "時程：1hr",
                                "gravity": "center",
                                "offsetStart": "8px",
                                "color": "#8E8E8E"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "text",
                                "text": "第二站"
                            },
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                "offsetEnd": "20px"
                            },
                            {
                                "type": "text",
                                "text": "08:00"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://i.imgur.com/VNeqIZ2.png",
                                "offsetStart": "45px"
                            },
                            {
                                "type": "text",
                                "text": "時程：1hr",
                                "gravity": "center",
                                "offsetStart": "8px",
                                "color": "#8E8E8E"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "text",
                                "text": "第三站"
                            },
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                "offsetEnd": "20px"
                            },
                            {
                                "type": "text",
                                "text": "09:00"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}


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
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text='hi', contents=contents))
    else:
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text="您好～請先點選下方選單中的開始進行葡萄酒選擇喔"))


# 執行
if __name__ == "__main__":
    app.run()
