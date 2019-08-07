from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
session_factory = sessionmaker(bind=db.engine)
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models, databaseUpdater

def updatePrices():
    databaseUpdater.update_price_table()

scheduler = BackgroundScheduler()

scheduler.add_job(updatePrices, 'interval', days=1)

try:
    scheduler.start()
except(KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
