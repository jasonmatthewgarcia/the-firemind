from flask import Flask, request
from app.models import fetch_card
import config
import requests

def _get_card_not_found_response(message):
    
    return "Sorry, but I can't find '{}'. Please try again.\n\nType 'help' to view instructions".format(message)

def _get_help_message():
    
    return "Type in the card you want to see prices on e.g. 'Farseek'.\n\nNo need to type any special characters(-,!')."

def _generate_elements(list_of_card_data):
    
    elements = []

    for card in list_of_card_data:

        element = {
            "title": "{} - {}".format(card.get('name'), card.get('set_name')),
            "image_url": card.get('image_url'),
            "subtitle": "Normal: ${}\nFoil: ${}".format(card.get('normal_price'), card.get('foil_price')),
            "default_action": {
                "type": "web_url",
                "url": card.get('image_url'),
                "webview_height_ratio": "full",
            },
            "buttons": [
                {
                    "type": "web_url",
                    "url": card.get('url'),
                    "title": "Get it @TCGPlayer",
                }
            ]
        }

        elements.append(element)

    return elements

def _send_message(recipient_id, message_payload):
    """Send a response to Facebook"""
    payload = {
        'message': message_payload,
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

def _get_card_if_it_exists(message):

    return fetch_card(message)

def _get_error_message_template(message):

    if message == 'help':
        return {'text' : _get_help_message()}
    else:
        return {'text' : _get_card_not_found_response(message)}

def _get_message_template(card_data):

    return {
        'attachment': {
            'type': 'template',
            'payload': {
                'template_type': 'generic',
                'elements': _generate_elements(card_data)
            }
        }
    }

def verify_webhook(req):
    if req.args.get("hub.verify_token") == config.VERIFY_TOKEN:
        print("Validated")
        return req.args.get('hub.challenge'), 200
    else:
        return 'Incorrect', 400

def respond(sender, message):

    card_data = _get_card_if_it_exists(message)
    
    if card_data:
        message_payload = _get_message_template(card_data)
    else:
        message_payload = _get_error_message_template(message)

    _send_message(sender, message_payload)

def is_user_message(message):

    return (message.get('message') and 
            message['message'].get('text') and
            not message['message'].get('is_echo'))