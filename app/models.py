from app import db, login, session_factory
from sqlalchemy.orm import scoped_session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from contextlib import contextmanager

from sqlalchemy.sql import text

@login.user_loader
def load_user(id):
    
    return Admin.query.get(int(id))

def bulk_insert_data(table, list_of_data):

    Session = scoped_session(session_factory)    
    Session.bulk_insert_mappings(table, list_of_data)
    Session.commit()
    Session.remove()

def fetch_card(name):

    Session = scoped_session(session_factory)
    sql = '''
    SELECT 
       c.name as card_name,
       c.imageUrl as image_url,
       c.url as url,
       s.name as set_name,
       p.midPrice as price,
       p.subTypeName as type
    FROM card c
       JOIN
       card_set s ON c.groupId = s.groupId
       JOIN
       price p ON c.productId = p.productId
    WHERE (c.cleanName = :param OR 
        c.name = :param) AND 
       s.isSupplemental = 0
       '''
    
    return Session.query(Card, CardSet, Price).from_statement(text(sql)).params(param=name).all()

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

    productId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(50))
    cleanName = db.Column(db.Text(50))
    imageUrl = db.Column(db.Text(100))
    groupId = db.Column(db.Integer)
    url = db.Column(db.Text(100))

    def __repr__(self):
        
        return '<id {}, name {}>'.format(self.productId, self.name)

    def getAllCardIdsFromDatabase(self, chunkSize=100):

        cards = self.query.all()
        cardIds = [card.productId for card in cards]

        chunks_of_cardIds = [cardIds[x:x+chunkSize] for x in range(0, len(cardIds), chunkSize)]

        return chunks_of_cardIds

class CardSet(db.Model):

    groupId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(50))
    isSupplemental = db.Column(db.Boolean)

    def __repr__(self):

        return '<id {}, name {}>'.format(self.groupId, self.name)

class Price(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer)
    midPrice = db.Column(db.Float)
    subTypeName = db.Column(db.VARCHAR(15))

    def __repr__(self):

        return '<id {}, normal_price {}>'.format(self.productId, self.marketPrice)