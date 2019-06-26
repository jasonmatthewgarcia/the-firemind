from flask import Flask, request

import requests
import time
import config

app = Flask(__name__)
app.config.from_pyfile('config.py')

from server import *

if __name__ == '__main__':
    app.run(debug=True)