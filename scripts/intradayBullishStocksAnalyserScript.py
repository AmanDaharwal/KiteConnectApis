from datetime import datetime


def getBullishStocksForNSE(kite, tradingSymbols, exchange='NSE'):

    symbol = []

    for tsymbols in tradingSymbols:

        # Get the list of NSE instruments
        nse_instruments = kite.ltp(exchange+":"+tsymbols)

        # Define the bullish criteria
        volume_threshold = 1000000  # Minimum volume threshold in shares
        percentage_change_threshold = 1  # Minimum percentage change in price

        # Iterate through each instrument
        for key, value in nse_instruments.items():
            instrument_token = value['instrument_token']

            current_date = datetime.now().strftime("%Y-%m-%d")
            print("Current date is "+current_date)

            # Fetch historical data for the instrument
            historical_data = kite.historical_data(instrument_token, current_date, current_date, interval='day',
                                                   continuous=False)

            # Extract relevant data
            close_prices = [data['close'] for data in historical_data]
            volumes = [data['volume'] for data in historical_data]

            # Calculate percentage change in price
            percentage_change = (close_prices[-1] - close_prices[0]) / close_prices[0] * 100

            # Check if the stock meets the bullish criteria
            if volumes[-1] > volume_threshold and percentage_change > percentage_change_threshold:
                symbol.append(tsymbols['tradingsymbol'])
                print(f"{tsymbols['tradingsymbol']} is bullish with a volume of {volumes[-1]} shares and a {percentage_change:.2f}% increase.")

        return symbol
