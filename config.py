import os

basedir = os.path.abspath(os.path.dirname(__file__))
TCGPlayer_version = 'v1.17.0'
BEARER_TOKEN = {'Authorization' : 'Bearer LaKBHVvyk4CKd-1ZM2ssCvhVAAfUSY5tqw57nay9IqekKi6WOp6b8TaoO7ICduJTgeOvL1gkk_QY1ltkGyindWyq9Yn5_ql6Z06r0vzjC8AT9M6bR_VLo6HIb4vXQEIwZabDKS1ZGsNIdzIx79NYAkLs6kqCIk7CGP2Th31Ea9Bug_1uCMUKpykd7KDf2grKoLy37PsYbrFKGTXqNDc-eB4VezNUeBfRCU8WhLwSkKFwQJTVzVPg7duisGgbfNThas_EgkuFV_DhWyfm82_gFISgkbqz5LUtS4n_BuoqQRv4ixX-T4aD083HidHkyjiadw4d4w'}
PAGE_ACCESS_TOKEN = 'EAAd8Oi7Wz3ABAJifYCQaNJCM1OCvlWsqaDVUQjFA87h4vq7D3yGxw5rZBWlZBtxYyCUfbx7bgtA5WDOfMCmjYTeAPjVnlBRVCQioJ5jjlrEBRuADl5gF2OlsF1T5vwx2faZBtzFtraXllAX1Rc3tzHxh11snOJ9FZCRn1Kk1bQZDZD'
VERIFY_TOKEN = 'secret'
FB_API_URL = 'https://graph.facebook.com/v3.3/me/messages'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database/firemind.db')
    SQLALCHEMY_TRACK_MODIFICATIONS= False