def transit():
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
    return contents
