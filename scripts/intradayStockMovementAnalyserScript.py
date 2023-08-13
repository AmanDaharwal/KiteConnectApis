from datetime import datetime, timedelta


def checkStockMovement(kite, symbol, period=30, exchange='NSE'):

    # Search for the stock symbol and get the instrument token
    instrument_tokens = kite.ltp(exchange+":" + symbol)
    instrument_token = instrument_tokens[exchange+":"+symbol]['instrument_token']

    print(f"The instrument token for {symbol} is {instrument_token}")

    # Calculate the start and end timestamps for the last 30 minutes
    end_time = datetime.now()
    start_time = end_time - timedelta(minutes=period)

    # Fetch historical data for the instrument
    historical_data = kite.historical_data(instrument_token, start_time, end_time, interval='minute')

    # Extract the closing prices from historical data
    closing_prices = [data['close'] for data in historical_data]

    # Check if the stock value is going upwards or downwards
    if closing_prices[0] > closing_prices[-1]:
        trend = 'Downwards'
    elif closing_prices[0] < closing_prices[-1]:
        trend = 'Upwards'
    else:
        trend = 'Stable'

    print(f"The stock value of {symbol} is trending {trend} over the last {period} minutes.")
    return trend

