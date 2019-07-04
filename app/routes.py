from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import Admin, Card
from werkzeug.urls import url_parse

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():

    payload = Card.query.all()
    return render_template('index.html', title='Home', payload=payload[0].name)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invaid username or password')
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