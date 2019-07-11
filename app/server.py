from flask import Flask, request
from app.models import fetch_card
import config
import requests

def get_bot_response(message):
    """This is just a dummy function, returning a variation of what
    the user said. Replace this function with one connected to chatbot."""
    # return "Card info in json {}".format(getProductInfo(message))
    return "Card = {}".format(message), 200
    # return "Dummy response {}".format(message)

def generate_elements(message):
    
    elements = []
    list_of_cards = fetch_card(message)

    for card in list_of_cards:

        element = {
            "title": "{} - {}".format(card['name'], card['set_name']),
            "image_url": card['image_url'],
            "subtitle": "{}".format(card['price']),
            "default_action": {
                "type": "web_url",
                "url": card['image_url'],
                "webview_height_ratio": "full",
            },
            "buttons": [
                {
                    "type": "web_url",
                    "url": card['url'],
                    "title": "Get it @TCGPlayer",
                }
            ]
        }

        elements.append(element)

    return elements

def send_message(recipient_id, text):
    """Send a response to Facebook"""
    payload = {
        'message': {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": generate_elements(text)
                }
            }
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }
    auth = {
        'access_token': config.PAGE_ACCESS_TOKEN
    }
    response = requests.post(
        config.FB_API_URL,
        params=auth,
        json=payload
    )

    return response.json(), 200

def verify_webhook(req):
    if req.args.get("hub.verify_token") == config.VERIFY_TOKEN:
        print("Validated")
        return req.args.get('hub.challenge'), 200
    else:
        return 'Incorrect', 400

def respond(sender, message):
    # response = get_bot_response(message)
    send_message(sender, message)

def is_user_message(message):

    return (message.get('message') and 
            message['message'].get('text') and
            not message['message'].get('is_echo'))