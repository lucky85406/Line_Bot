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
    "size": "mega",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "FROM",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "Akihabara",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "TO",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "Shinjuku",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                ]
            }
        ],
        "paddingAll": "20px",
        "backgroundColor": "#0367D3",
        "spacing": "md",
        "height": "154px",
        "paddingTop": "22px"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "Total: 1 hour",
                "color": "#b7b7b7",
                "size": "xs"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "20:30",
                        "size": "sm",
                        "gravity": "center"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "cornerRadius": "30px",
                                "height": "12px",
                                "width": "12px",
                                "borderColor": "#EF454D",
                                "borderWidth": "2px"
                            },
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Akihabara",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                ],
                "spacing": "lg",
                "cornerRadius": "30px",
                "margin": "xl"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "width": "2px",
                                        "backgroundColor": "#B7B7B7"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "flex": 1
                            }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "text",
                        "text": "Walk 4min",
                        "gravity": "center",
                        "flex": 4,
                        "size": "xs",
                        "color": "#8c8c8c"
                    }
                ],
                "spacing": "lg",
                "height": "64px"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "20:34",
                                "gravity": "center",
                                "size": "sm"
                            }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "cornerRadius": "30px",
                                "width": "12px",
                                "height": "12px",
                                "borderWidth": "2px",
                                "borderColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Ochanomizu",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                ],
                "spacing": "lg",
                "cornerRadius": "30px"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "width": "2px",
                                        "backgroundColor": "#6486E3"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "flex": 1
                            }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "text",
                        "text": "Metro 1hr",
                        "gravity": "center",
                        "flex": 4,
                        "size": "xs",
                        "color": "#8c8c8c"
                    }
                ],
                "spacing": "lg",
                "height": "64px"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "20:40",
                        "gravity": "center",
                        "size": "sm"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "cornerRadius": "30px",
                                "width": "12px",
                                "height": "12px",
                                "borderColor": "#6486E3",
                                "borderWidth": "2px"
                            },
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Shinjuku",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                ],
                "spacing": "lg",
                "cornerRadius": "30px"
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
