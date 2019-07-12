import config, requests

def getAllPricesByChunk(chunks_of_cardIds, session):

    list_of_prices = []
    for chunk in chunks_of_cardIds:

        cardIds = ','.join(map(str, chunk))
        request = "http://api.tcgplayer.com/{}/pricing/product/{}".format(config.TCGPlayer_version, cardIds)
        fetched_prices = _fetchCardDataFromTCGPlayer(session, request)
        list_of_prices += fetched_prices

        print("{} prices fetched".format(len(list_of_prices)))

    return list_of_prices

def getBulkCardData(session, request, params, offset):

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