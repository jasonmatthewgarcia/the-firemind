import os

basedir = os.path.abspath(os.path.dirname(__file__))
TCGPLAYER_VERSION = 'v1.27.0'
BEARER_TOKEN = {'Authorization' : 'HOb5CIvjb1WttImHl69hutd1DqEy7zfUuymvIUF2G8gZelYDZjbSXV4g0owaSmjsMrHc278-SkvSGS--NSb8ogtm8wu0NMd3XiOHBchSwMtZL1q9jM_jOBrHWf89OnjShxWkIH-s4I7UfgbPzeq_AtoFW2kkolzVslE-8GNypK_fg412X7LXWciKHtAKmNX94KrBeQmYf6pMndOJ4fERNn4FoOZ29kMfSZfQ6G_jXAbTWkCXanPB_FM-Na9k3F15yG4LLCr4fbIXFog6HVeKu-3_IQa6tb1DUOV8et1eqlbRfSHk3luAZuGYBTP0Ckq9GKGN6Q'}
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