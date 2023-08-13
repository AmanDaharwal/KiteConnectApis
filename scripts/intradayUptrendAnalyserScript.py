from datetime import datetime, timedelta


def getUptrendingStocksForNSE(kite, tradingSymbols, period=30, exchange='NSE'):
    symbol = []

    for tsymbols in tradingSymbols:

        # Get the list of NSE instruments
        nse_instruments = kite.ltp(exchange + ":" + tsymbols)

        # Fetch historical data for each instrument
        for key, value in nse_instruments.items():
            instrument_token = value['instrument_token']

            end_time = datetime.now()
            start_time = end_time - timedelta(minutes=period)

            historical_data = kite.historical_data(instrument_token, start_time, end_time, interval='minute',
                                                   continuous=False)

            # Calculate the percentage change over the period
            start_price = historical_data[0]['close']
            end_price = historical_data[-1]['close']
            percentage_change = (end_price - start_price) / start_price * 100

            # Check if the stock is trending upwards
            if percentage_change > 0:
                symbol.append(tsymbols)
                print(f"{tsymbols} is trending upwards with a {percentage_change:.2f}% increase.")

    return symbol
