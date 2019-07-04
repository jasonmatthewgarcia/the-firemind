from app import app, db
from app.models import Admin, Card, CardSet, Price

@app.shell_context_processor
def make_shell_context():
    return {'db' : db, 'Admin' : Admin, 'Card' : Card, 'CardSet' : CardSet, 'Price' : Price}