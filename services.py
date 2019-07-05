from app import app, db
from app.models import Card
import pandas as pd
import config, requests

def _getAllCardIds(chunkSize):

    cards = Card.query.all()
    cardIds = [card.id for card in cards]

    chunks_of_cardIds = [cardIds[x:x+chunkSize] for x in range(0, len(cardIds), chunkSize)]

    return chunks_of_cardIds

def getAllPricesByChunk(chunks_of_cardIds, session):

    list_of_prices = []
    for chunk in chunks_of_cardIds:

        cardIds = ','.join(map(str, chunk))
        response = session.get("http://api.tcgplayer.com/{}/pricing/product/{}".format(config.TCGPlayer_version, cardIds))
        prices = response.json()['results']

        list_of_prices += prices

    return list_of_prices

def updateCardDataInDatabase(session, table_to_update, current_record_count):

    offset = current_record_count
    catalog_type = {'card' : 'products', 'card_set' : 'groups'}
    data = []

    while True:
        list_of_data = fetchCardDataFromTCG(session, catalog_type[table_to_update], offset)
        data += list_of_data
        offset += 100
        if not list_of_data:
            break
        
    return data

def fetchCardDataFromTCG(session, catalog_type, offset):

    data = {'categoryId' : 1, 'productTypes' : 'Cards', 'offset' : offset, 'limit' : 100}
    response = session.get("http://api.tcgplayer.com/{}/catalog/{}".format(config.TCGPlayer_version, catalog_type), params=data)
    return response.json()['results']



session = requests.Session()
session.headers.update(config.BEARER_TOKEN)

# x = _getAllCardIds(100)

cards = updateCardDataInDatabase(session, 'card', 43000)
sets = updateCardDataInDatabase(session, 'card_set', 200)


# y = getAllPricesByChunk(x, session)
# print(y)