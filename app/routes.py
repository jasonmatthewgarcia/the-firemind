from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import Admin, Card, CardSet, Price, bulk_insert_data, replace_entire_table, fetch_card
from app.services import *
from app.server import *
from werkzeug.urls import url_parse

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():

    return render_template('index.html', title='Home')

@app.route('/update_prices', methods=['GET', 'POST'])
@login_required
def update_prices():

    session = init_session()
    cards = Card()
    list_of_cardIds = cards.getAllCardIdsFromDatabase()
    list_of_prices = getAllPricesByChunk(list_of_cardIds, session)
    replace_entire_table(Price, list_of_prices)

    return render_template('index.html', title='Home', payload="{} card prices updated".format(len(list_of_prices)))

@app.route('/update_all_data', methods=['GET', 'POST'])
@login_required
def update_all_data():

    session = init_session()
    default_params = {'categoryId' : 1, 'productTypes' : 'Cards', 'limit' : 100}
    list_of_cards = getBulkCardData(session, config.TCGPLAYER_CARD_API_URL, default_params)
    list_of_card_sets = getBulkCardData(session, config.TCGPLAYER_CARD_SET_API_URL, default_params)

    replace_entire_table(Card, list_of_cards)
    replace_entire_table(CardSet, list_of_card_sets)

    update_prices()
    
    return render_template('index.html', title='Home', payload="{} cards updated".format(len(list_of_cards)))

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