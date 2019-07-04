from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    
    return Admin.query.get(int(id))

class Admin(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(64))
    password_hash = db.Column(db.VARCHAR(128))

    def set_password(self, password):

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(self.password_hash, password)
        

    def __repr__(self):

        return '<User {}>'.format(self.username)

class Card(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(50))
    clean_name = db.Column(db.VARCHAR(50))
    image_url = db.Column(db.VARCHAR(100))
    url = db.Column(db.VARCHAR(100))

    def __repr__(self):

        return '<id {}, name {}>'.format(self.id, self.name)

class CardSet(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(50))

    def __repr__(self):

        return '<id {}, name {}>'.format(self.id, self.name)

class Price(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer)
    normal_price = db.Column(db.Float)
    foil_price = db.Column(db.Float)

    def __repr__(self):

        return '<id {}, normal_price {}>'.format(self.id, self.normal_price)