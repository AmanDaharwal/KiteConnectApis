from kiteconnect import KiteConnect
import statistics as stats
from datetime import datetime, timedelta


def checkBollingerBandCondition(kite, symbol, period=30, exchange='NSE'):
    # Search for the stock symbol and get the instrument token
    instrument_tokens = kite.ltp(exchange + ":" + symbol)
    instrument_token = instrument_tokens[exchange + ":" + symbol]['instrument_token']

    print(f"The instrument token for {symbol} is {instrument_token}")

    end_time = datetime.now()
    start_time = end_time - timedelta(minutes=period)

    # Fetch historical data for the instrument
    historical_data = kite.historical_data(instrument_token, start_time, end_time, interval='minute')
    checkBollingerBandConditionForHistoricalData(historical_data, symbol)


def checkBollingerBandConditionForHistoricalData(historical_data, symbol):
    # Extract the closing prices from historical data
    closing_prices = [data['close'] for data in historical_data]

    # Calculate the Bollinger Bands
    window = 20  # Window size for calculating moving average and standard deviation
    standard_deviations = []
    moving_averages = []

    for i in range(window, len(closing_prices)):
        window_data = closing_prices[i - window: i]
        moving_average = stats.mean(window_data)
        moving_averages.append(moving_average)
        standard_deviation = stats.stdev(window_data)
        standard_deviations.append(standard_deviation)

    # Calculate the current price and Bollinger Bands values
    current_price = closing_prices[-1]
    upper_band = moving_averages[-1] + (2 * standard_deviations[-1])
    lower_band = moving_averages[-1] - (2 * standard_deviations[-1])

    # Analyze the current price with respect to the Bollinger Bands
    if current_price > upper_band:
        signal = "Overbought"
    elif current_price < lower_band:
        signal = "Oversold"
    else:
        signal = "Neutral"

    print(f"The {symbol} current price is {signal} based on Bollinger Bands analysis.")

    return signal
