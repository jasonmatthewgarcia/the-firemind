import os

basedir = os.path.abspath(os.path.dirname(__file__))
TCGPLAYER_VERSION = 'v1.27.0'
BEARER_TOKEN = {'Authorization' : 'Bearer gY-vkATV5si9s9AqITWrlBQYcwqexMgCNe_9LWLS8ny2LxAZU6FMyBf8yu3jEysKWOABF9q3Hg5xSjCP_4hwLAIsGAxpXd51hCEpmp9YfOm5FuqwHtuuvze2NHoFVOTXyeXwA729MFjW4kccJg6ACnSjSQiur44LsTflHYiwvZUQTzZPJGA4FNVwT4Xyi75JKx_Jig2FoZIWvEmfkfIVm693c-K_1HcNr9Q4joqvDXJsvjZuOm1EgjlDrgIj4bLb7BiRU5B0lYL7h2y4kQ35-Nndp2q3BoEhpIiDXUK82z4OJaUzugoWR-wq5kySYmQcSiqYLg'}
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