import requests, config, time

headers = {'Authorization' : config.BEARER_TOKEN}

def getProductInfo(productName):

    list_of_cards = []
    s = requests.Session()
    s.headers.update(headers)
    products_per_set = getProducts(productName, s)
    normal_emoji = u'\U0001F516'
    foil_emoji = u'\U0001F308'

    for product in products_per_set:    

        set_name = _getProductGroup(product['groupId'], s)
        card_prices = _getProductPrice(product['productId'], s)
        card = {
            'product_name' : product['productName'],
            'set_name' : set_name,
            'image_url' : product['image'],
            'url' : product['url'],
            'normal_market_price' : "{}: ${}".format(normal_emoji, card_prices['normal_price']),
            'foil_market_price' : "{}: ${}".format(foil_emoji, card_prices['foil_price'])
        }

        list_of_cards.append(card)
    
    return list_of_cards

def getProducts(productName, session):

    data = {'categoryId' : 1, 'productTypes' : 'Cards', 'productName' : productName}
    request = session.get("http://api.tcgplayer.com/v1.9.0/catalog/products", params=data)
    return request.json()['results']

def _getProductPrice(productId, session):

    prices = session.get("https://api.tcgplayer.com/v1.9.0/pricing/product/{0}".format(productId))
    card_prices = prices.json()
    card_price = {}

    for price in card_prices['results']:

        if price['subTypeName'] == "Foil":
            card_price['foil_price'] = price['midPrice']
        else:
            card_price['normal_price'] = price['midPrice']

    return card_price


def _getProductGroup(groupId, session):
    
    
    groups = session.get("http://api.tcgplayer.com/v1.9.0/catalog/groups/{0}".format(groupId))
    set_name = groups.json()['results']
    
    return set_name[0]['name']

# card_name = input("Card name: ")
# start = time.time()
# print(getProductInfo(card_name))
# end = time.time()
# print(end-start)