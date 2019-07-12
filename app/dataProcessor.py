

def splitListOfDataIntoChunks(list_of_data, chunk_size=100):

    chunks_of_data = [list_of_data[x:x+chunk_size] for x in range(0, len(list_of_data), chunk_size)]
    
    return chunks_of_data

def formatFetchedCardData(list_of_card_data):

    cards = {}

    for card in list_of_card_data:

        card_data