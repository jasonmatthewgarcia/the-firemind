from app import db, login, session_factory
from app.dataProcessor import splitListOfDataIntoChunks, formatFetchedCardData
from sqlalchemy.orm import scoped_session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from contextlib import contextmanager

@login.user_loader
def load_user(id):
    
    return Admin.query.get(int(id))

@contextmanager
def get_db_session():
    try:
        Session = scoped_session(session_factory)
        yield Session
    except Exception as e:
        print(e)
        Session.rollback()
    finally:
        Session.remove()

def bulk_insert_data(table, list_of_data):

    with get_db_session() as Session:
        Session.bulk_insert_mappings(table, list_of_data)
        Session.commit()

def replace_entire_table(table, list_of_data):

    with get_db_session() as Session:
        Session.query(table).delete()
        Session.bulk_insert_mappings(table, list_of_data)
        Session.commit()


def fetch_card(name):

    with get_db_session() as Session:
        results = Session.query(Card).filter((Card.cleanName == name) | (Card.name == name)).limit(10).all()
        list_of_card_data = formatFetchedCardData(results)

        return list_of_card_data

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
    __tablename__ = 'card'
    productId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(50))
    cleanName = db.Column(db.Text(50))
    imageUrl = db.Column(db.Text(100))
    groupId = db.Column(db.Integer, db.ForeignKey('card_set.groupId'))
    url = db.Column(db.Text(100))

    card_set = db.relationship('CardSet', backref='card' ,uselist=False)
    prices = db.relationship('Price', backref='card', lazy='joined')

    def __repr__(self):
        
        return '<id {}, name {}>'.format(self.productId, self.name)

    def getAllCardIdsFromDatabase(self, chunkSize=100):

        cards = self.query.all()
        cardIds = [card.productId for card in cards]

        chunks_of_cardIds = splitListOfDataIntoChunks(cardIds)

        return chunks_of_cardIds

class CardSet(db.Model):
    __tablename__ = 'card_set'
    groupId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(50))
    isSupplemental = db.Column(db.Boolean)

    def __repr__(self):

        return '<id {}, name {}>'.format(self.groupId, self.name)

class Price(db.Model):
    __tablename__ = 'price'
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('card.productId'))
    midPrice = db.Column(db.Float)
    subTypeName = db.Column(db.VARCHAR(15))

    def __repr__(self):

        return '<id {}, normal_price {}>'.format(self.productId, self.midPrice)