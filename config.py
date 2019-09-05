import os

basedir = os.path.abspath(os.path.dirname(__file__))
TCGPLAYER_VERSION = 'v1.32.0'
BEARER_TOKEN = {'Authorization' : 'Bearer 0ePIp1dq2j6QlN2AT4O1PV_sFWcWvJPusXEiOQjGZlkDOQ-2KsfrgCa876JsQbsbxkv7TbAyvBl16-S5paiJfBqVdmJBab80njkgV7Ed6E0-o5MKsw_KW1RHISmD_VHk-gYS6OnFCUqvPSMhyfnU43tMEgMjhg71Y67rm6uev_jEU7f71E6R64YCDIqmejqCKO96bTOC5_cBNYhyF7t2_bS1Vy2vsBQ8Q3cWunKrR5ahaiO6CzLyhKVLBH2FuXezs8yxzBvavO985U6p_oDcI6Q0E0fGwx9eZlpTQN6eZb-DegEoOqjIyQ-MKEMLhq03Gmo88Q'}
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