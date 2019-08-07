from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import Admin, Card, CardSet, Price
from app.databaseUpdater import *
from app.services import *
from app.server import *
from werkzeug.urls import url_parse

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():

    return render_template('index.html', title='Home')

@app.route('/update_prices', methods=['GET'])
@login_required
def update_prices():

    update_price_table()

    return render_template('index.html', title='Home', payload="Prices updated")

@app.route('/update_all_data', methods=['GET'])
@login_required
def update_all_data():

    update_all_tables()

    return render_template('index.html', title='Home', payload="Data updated")

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(admin)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('login'))

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():

    logout_user()
    return redirect(url_for('index'))

@app.route('/webhook', methods=['GET', 'POST'])
def listen():

    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text)

        return "ok", 200