import os

basedir = os.path.abspath(os.path.dirname(__file__))
TCGPLAYER_VERSION = 'v1.32.0'
BEARER_TOKEN = {'Authorization' : 'Bearer JCgAN1Q1ZPjraMgT0Qp3HFbAiu9Q_XVGYbw4NnCDl2azvvD7ZtRcfLRE78sNse_HZOlT8mlFTQwfXKNmUWnJmW3ZZ9No2iWf9yfONBDNYRj4kL1ibbY8EaWzdhf1ReZuMTzFN06Z8n56l4Os-yESJfls7cJWeoERu2eHV2jHqV1zr3486YDTtGRdO6-rMfooN8P_7TkAWr2MzA0_ASvmhI75scQnA2bDZANGz0vxzXo-00nDtwSD_CHQW8u2RZMPfKejO9L9eNCOM18M7YuchBCrCdAePX5tYQ3wf28FAL_lKR8gXlJY54QGj99nWmEsoRm9EQ'}
PAGE_ACCESS_TOKEN = 'EAAd8Oi7Wz3ABAJifYCQaNJCM1OCvlWsqaDVUQjFA87h4vq7D3yGxw5rZBWlZBtxYyCUfbx7bgtA5WDOfMCmjYTeAPjVnlBRVCQioJ5jjlrEBRuADl5gF2OlsF1T5vwx2faZBtzFtraXllAX1Rc3tzHxh11snOJ9FZCRn1Kk1bQZDZD'
VERIFY_TOKEN = 'secret'

TCGPLAYER_CARD_API_URL = 'http://api.tcgplayer.com/{}/catalog/products'.format(TCGPLAYER_VERSION)
TCGPLAYER_CARD_SET_API_URL = 'http://api.tcgplayer.com/{}/catalog/groups'.format(TCGPLAYER_VERSION)
TCGPLAYER_PRICE_API_URL = 'http://api.tcgplayer.com/{}/pricing/product/'.format(TCGPLAYER_VERSION)
FB_API_URL = 'https://graph.facebook.com/v3.3/me/messages'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database/firemind.db')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
