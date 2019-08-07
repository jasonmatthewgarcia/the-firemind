from app.models import Card, CardSet, Price, bulk_insert_data, replace_entire_table, fetch_card
from app.services import *

def update_price_table():

    session = init_session()
    cards = Card()
    list_of_cardIds = cards.getAllCardIdsFromDatabase()
    list_of_prices = getAllPricesByChunk(list_of_cardIds, session)
    replace_entire_table(Price, list_of_prices)

def update_all_tables():

    session = init_session()
    default_params = {'categoryId' : 1, 'productTypes' : 'Cards', 'limit' : 100}
    list_of_cards = getBulkCardData(session, config.TCGPLAYER_CARD_API_URL, default_params)
    list_of_card_sets = getBulkCardData(session, config.TCGPLAYER_CARD_SET_API_URL, default_params)

    replace_entire_table(Card, list_of_cards)
    replace_entire_table(CardSet, list_of_card_sets)

    update_price_table()

def test():

    print("TESTING WORKED")