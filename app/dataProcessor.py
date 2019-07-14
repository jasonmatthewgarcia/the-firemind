

def splitListOfDataIntoChunks(list_of_data, chunk_size=100):

    chunks_of_data = [list_of_data[x:x+chunk_size] for x in range(0, len(list_of_data), chunk_size)]
    
    return chunks_of_data

def formatFetchedCardData(results):

    cards = []
    
    for card in results:

        card_data = {}

        card_data['name'] = card.name
        card_data['image_url'] = card.imageUrl
        card_data['url'] = card.url
        card_data['set_name'] = card.card_set.name
        
        for price in card.prices:
            
            if price.subTypeName == 'Foil':
                card_data['foil_price'] = price.midPrice
            else:
                card_data['normal_price'] = price.midPrice
        
        cards.append(card_data)

    return cards