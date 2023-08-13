

def checkVolatabilty(kite, symbol, exchange):

    # Define the instrument token for the desired stock or instrument
    instrument_token = exchange+':'+symbol

    # Retrieve the Market Depth using the instrument token
    market_depth = kite.quote([instrument_token])

    # Extract the buy and sell quantities from the Market Depth
    buy_quantity = market_depth[instrument_token]['depth']['buy'][0]['quantity']
    sell_quantity = market_depth[instrument_token]['depth']['sell'][0]['quantity']

    # Print the total number of buy bids and sell offers
    print("Buy Bids: ", buy_quantity)
    print("Sell Offers: ", sell_quantity)

    volatabilty = (buy_quantity/sell_quantity) * 100
    if volatabilty>20:
        return True
    else:
        return False