from kiteconnect import KiteConnect
import pandas as pd


def calculate_target_hitting_probablity(kite, symbol, target_price, exchange='NSE'):
    # Define the instrument token for the desired stock or instrument
    # Search for the stock symbol and get the instrument token
    instrument_tokens = kite.ltp(exchange + ":" + symbol)
    instrument_token = instrument_tokens[exchange + ":" + symbol]['instrument_token']


    # Set the number of historical data points to fetch
    num_points = 100  # Adjust as per your requirement

    # Fetch historical data for the stock
    historical_data = kite.historical_data(instrument_token, "2022-01-01", "2022-12-31", "day")

    # Create a DataFrame from the historical data
    df = pd.DataFrame(historical_data)

    # Extract the closing prices
    closing_prices = df['close'].tail(num_points)

    # Calculate the probability of hitting the target price
    hit_count = sum(closing_prices >= target_price)
    probability = hit_count / num_points

    # Print the probability
    print("Probability of hitting the target price:", probability)
