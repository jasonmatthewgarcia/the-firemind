import os

basedir = os.path.abspath(os.path.dirname(__file__))
TCGPlayer_version = 'v1.27.0'
BEARER_TOKEN = {'Authorization' : 'Bearer h9O2QA_H2NE1FUZ2QOeDfhe5d7wS8wzy1f2NkksoANtQbsV0N4rx5BrwN11AcTtAuW7-E-m-k55lKnb62n97nnFdygW3-7r9T1Jg8eFifrTcirTaDBbR3fVdSi736rh2U_KSQV8-6JlHxmoCWdgNjwkfLz3hochvjXODDnfcOx-I6FkpItfywKx0Zg8-oBGWFX0fyZIGtJYWlFit4mtzlyc6qVFWZV26uE5dQyN_p2UEkXscj9pho3--qfwT_suakEZNr6vANI9jcKCG0DyiVVkvRDdBote0LSML0gZhHbpUBahwYsLQLLSdh1blCS5YVp31Lg'}
PAGE_ACCESS_TOKEN = 'EAAd8Oi7Wz3ABAJifYCQaNJCM1OCvlWsqaDVUQjFA87h4vq7D3yGxw5rZBWlZBtxYyCUfbx7bgtA5WDOfMCmjYTeAPjVnlBRVCQioJ5jjlrEBRuADl5gF2OlsF1T5vwx2faZBtzFtraXllAX1Rc3tzHxh11snOJ9FZCRn1Kk1bQZDZD'
VERIFY_TOKEN = 'secret'
FB_API_URL = 'https://graph.facebook.com/v3.3/me/messages'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database/firemind.db')
    SQLALCHEMY_TRACK_MODIFICATIONS= False