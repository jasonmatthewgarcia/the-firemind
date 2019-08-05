import config, requests
from app.models import Card, CardSet, Price, bulk_insert_data, replace_entire_table

def getAllPricesByChunk(chunks_of_cardIds, session):

    list_of_prices = []
    for chunk in chunks_of_cardIds:

        cardIds = ','.join(map(str, chunk))
        request = config.TCGPLAYER_PRICE_API_URL + cardIds
        fetched_prices = _fetchCardDataFromTCGPlayer(session, request)
        list_of_prices += fetched_prices

        print("{} prices fetched".format(len(list_of_prices)))

    return list_of_prices

def getBulkCardData(session, request, params, offset=0):

    params['offset'] = offset
    list_of_data = []

    while True:

        fetched_data = _fetchCardDataFromTCGPlayer(session, request, params)
        list_of_data += fetched_data
        params['offset'] += 100
        
        print("{} results fetched".format(params['offset']))

        if not fetched_data:
            break
    
    return list_of_data


def _fetchCardDataFromTCGPlayer(session, request, optionalParams=None):

    if optionalParams:
        response = session.get(request, params=optionalParams)
    else:
        response = session.get(request)

    return response.json()['results']

def init_session():

    session = requests.Session()
    session.headers.update(config.BEARER_TOKEN)

    return session
