import requests, config, time

headers = {'Authorization' : config.BEARER_TOKEN}

def getProductInfo(productName):

    list_of_cards = []
    session = requests.Session()
    session.headers.update(headers)
    products_per_set = getProducts(productName, session)
    normal_emoji = u'\U0001F516'
    foil_emoji = u'\U0001F308'

    for product in products_per_set:    

        set_name = _getProductGroup(product['groupId'], session)
        card_prices = _getProductPrice(product['productId'], session)
        card = {
            'product_name' : product['name'],
            'set_name' : set_name,
            'image_url' : product['imageUrl'],
            'url' : product['url'],
            'normal_market_price' : "{}: ${}".format(normal_emoji, card_prices['normal_price']),
            'foil_market_price' : "{}: ${}".format(foil_emoji, card_prices['foil_price'])
        }

        list_of_cards.append(card)
    
    return list_of_cards

def getProducts(name, session):

    data = {'categoryId' : 1, 'productTypes' : 'Cards', 'productName' : name}
    response = session.get("http://api.tcgplayer.com/v1.17.0/catalog/products", params=data)
    products = response.json()['results']
    
    return products

def _getProductPrice(productId, session):

    response = session.get("https://api.tcgplayer.com/v1.17.0/pricing/product/{0}".format(productId))
    card_prices = response.json()['results']
    card_price = {}

    for price in card_prices:

        if price['subTypeName'] == "Foil":
            card_price['foil_price'] = price['midPrice']
        else:
            card_price['normal_price'] = price['midPrice']

    return card_price


def _getProductGroup(groupId, session):
    
    response = session.get("http://api.tcgplayer.com/v1.17.0/catalog/groups/{0}".format(groupId))
    [set_name] = response.json()['results']

    return set_name['name']
    

# card_name = input("Card name: ")
# start = time.time()
# print(getProductInfo(card_name))
# end = time.time()
# print(end-start)