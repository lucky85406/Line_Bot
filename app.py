from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)

configuration = Configuration(access_token='BedaiCocJPX00F/9FaqlB9DjzZHtviqXZLo5LZNFO6dVSaLs52kaZm6jkQNy8IWNI/ozkRIFFqrxaMC8qLim1Uu0/G3I3TyXBCZ8ZmmuRW+CIEiP9wle1vHYEKll0XFxYUrjB5c8KgOeuSN+V9Ev+wdB04t89/1O/w1cDnyilFU=')  # YOUR_CHANNEL_ACCESS_TOKEN
handler = WebhookHandler('3861ce04f88b821a5e7199958d42459e')  # YOUR_CHANNEL_SECRET


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
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )


if __name__ == "__main__":
    app.run()
