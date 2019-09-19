import os

basedir = os.path.abspath(os.path.dirname(__file__))
TCGPLAYER_VERSION = 'v1.32.0'
BEARER_TOKEN = {'Authorization' : 'Bearer Xgv6k8exVq566Ssl0Nql65iVLxW-81WOVYl9xwKfscWSA54fEwUvk4PuOWHTy52NztzJ2qLFBRqith8b7xYZB8ZlJK1HcrDjAks4FUYtSF0gcqWlfpsN2JyByAXjPPbmFWwCeMETBcVgwPB3KNVmKuyh03vBNRRwdWm6GElp3Z1jFFQH2xCCIsdwkONwmEAZ08MDHunhMEGynKGCJxXLRooDvLPC81zraJkmCjf4i-Q8IijNlSzi_tKCgWoaeg2Lxucbj41Jsj9ccK_45HzBTd8jwjOts10b5CXx4-HJCOR2cNmAwwiydrEKVsNCHxuImbDxgw'}
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
