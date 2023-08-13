from kiteconnect import KiteConnect
from datetime import datetime, timedelta


def getListOfHighlyVolatileStocks(kite, exchange):

    # Get current date and time
    now = datetime.now()

    # Calculate the start time for fetching past hour data (subtract 1 hour)
    start_time = now - timedelta(hours=1)

    # Format the start and end timestamps in the required format
    end_time = datetime.now()
    start_time = end_time - timedelta(minutes=60)

    # Fetch historical data for all instruments in the exchange for the past hour
    historical_data = kite.historical_data(instrument_token=exchange+':*', from_date=start_time,
                                           to_date=end_time, interval='minute')

    # Calculate the volatility for each instrument
    volatility_threshold = 0.02  # Set the volatility threshold as per your requirement

    volatile_stocks = []

    for instrument_data in historical_data:
        instrument_token = instrument_data['instrument_token']
        ohlc_data = instrument_data['ohlc']
        close_prices = [ohlc['close'] for ohlc in ohlc_data]

        price_range = max(close_prices) - min(close_prices)
        volatility = price_range / close_prices[-1]

        if volatility >= volatility_threshold:
            volatile_stocks.append(instrument_token)

    # Print the list of highly volatile stocks
    print("Highly Volatile Stocks:")
    for stock in volatile_stocks:
        print(stock)
