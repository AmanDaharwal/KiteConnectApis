from kiteconnect import KiteConnect
import statistics as stats
from datetime import datetime, timedelta


def checkSupertrendCondition(kite, symbol, period=30, exchange='NSE'):
    # Search for the stock symbol and get the instrument token
    instrument_tokens = kite.ltp(exchange + ":" + symbol)
    instrument_token = instrument_tokens[exchange + ":" + symbol]['instrument_token']

    print(f"The instrument token for {symbol} is {instrument_token}")

    # Calculate the start and end timestamps for the last 30 minutes
    end_time = datetime.now()
    start_time = end_time - timedelta(minutes=period)

    # Fetch historical data for the instrument
    historical_data = kite.historical_data(instrument_token, start_time, end_time, interval='minute')
    checkSupertrendConditionForHistoricalData(historical_data)


def checkSupertrendConditionForHistoricalData(historical_data):
    # Extract the closing prices from historical data
    closing_prices = [data['close'] for data in historical_data]

    # Calculate the ATR (Average True Range)
    high_prices = [data['high'] for data in historical_data]
    low_prices = [data['low'] for data in historical_data]
    close_prices = [data['close'] for data in historical_data]

    high_low_diff = [high - low for high, low in zip(high_prices, low_prices)]
    high_close_diff = [abs(high - close) for high, close in zip(high_prices, close_prices)]
    low_close_diff = [abs(low - close) for low, close in zip(low_prices, close_prices)]

    true_range = [max(high_low, high_close, low_close) for high_low, high_close, low_close in
                  zip(high_low_diff, high_close_diff, low_close_diff)]
    average_true_range = stats.mean(true_range)

    # Calculate the Supertrend indicator
    multiplier = 2  # Multiplier for calculating upper and lower bands
    supertrend = []
    upper_band = []
    lower_band = []

    for i in range(len(closing_prices)):
        if i == 0:
            supertrend.append(closing_prices[i])
            upper_band.append(closing_prices[i] + (multiplier * average_true_range))
            lower_band.append(closing_prices[i] - (multiplier * average_true_range))
        else:
            if closing_prices[i] > upper_band[i - 1]:
                supertrend.append(lower_band[i - 1])
                upper_band.append(closing_prices[i] + (multiplier * average_true_range))
                lower_band.append(closing_prices[i] - (multiplier * average_true_range))
            else:
                supertrend.append(upper_band[i - 1])
                upper_band.append(upper_band[i - 1] + (multiplier * average_true_range))
                lower_band.append(lower_band[i - 1] + (multiplier * average_true_range))

    # Analyze the Supertrend indicator for entry and exit points
    entry_point = None
    exit_point = None

    if closing_prices[-1] > supertrend[-1]:
        entry_point = "Buy"
    elif closing_prices[-1] < supertrend[-1]:
        entry_point = "Sell"

    if closing_prices[-2] > supertrend[-2] and closing_prices[-1] < supertrend[-1]:
        exit_point = "Exit Buy"
    elif closing_prices[-2] < supertrend[-2] and closing_prices[-1] > supertrend[-1]:
        exit_point = "Exit Sell"

    print(f"Entry Point: {entry_point}")
    print(f"Exit Point: {exit_point}")
