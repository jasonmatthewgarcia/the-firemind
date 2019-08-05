import os

basedir = os.path.abspath(os.path.dirname(__file__))
TCGPLAYER_VERSION = 'v1.27.0'
BEARER_TOKEN = {'Authorization' : 'Bearer eQe-bSSAMojNJCWvwjSgYFT3cYIpRUJWI5PYJ0MoVC9hPN4IIk1SgpIolBkIJpOaDzFGTyzHOFQ2mYkkw0jOa8j9gCYc50RZ7unuhMTeobetsIMIe6U7zMN5J-Vao7PHgaAFVNLMyWsDF_dGgRecOtuzUS8bGIdOYhhUJCyKaOYAt-f4RomHZ4O_whh1hjfli6ForQMTjwIh7w8wzNcOnjRiY__Jym0E5dhGsJ6xn4cBgfq1EO5szC4sjeMtLXXIYRKEK92kjOdLp-KMJuI-6bFer7aXmnjR9QVxFqTgLnBs7q2D_g-yrGxZlOVYMxL29xQsFA'}
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