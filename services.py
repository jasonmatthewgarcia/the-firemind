from app import app
from app.models import Card
import config, requests

def getAllCardIds():

    cards = Card.query.all()

    cardIds = []
    for card in cards:

        cardIds.append(card.id)

    chunks_of_cardIds = [cardIds[x:x+100] for x in range(0, len(cardIds), 100)]

    return chunks_of_cardIds

def getAllPricesByChunk(chunks_of_cardIds, session):

    list_of_prices = []
    for chunk in chunks_of_cardIds:

        cardIds = ','.join(map(str, chunk))
        response = session.get("http://api.tcgplayer.com/{}/pricing/product/{}".format(config.TCGPlayer_version, cardIds))
        prices = response.json()['results']

        list_of_prices.append(prices)
        continue
    
    return list_of_prices

session = requests.Session()
session.headers.update(config.BEARER_TOKEN)

x = getAllCardIds()

y = getAllPricesByChunk(x, session)
print(y)