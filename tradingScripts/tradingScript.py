from commons.getLatestPremium import get_latest_premium
from commons.placeOrder import place_order
from commons.getOrderStatus import get_order_status
import time


# Place a market buy order function
def place_market_buy_order(kite, symbol, exchange):
    order_id = place_order(
        kite=kite,
        variety=kite.VARIETY_REGULAR,
        exchange=exchange,
        tradingsymbol=symbol,
        transaction_type=kite.TRANSACTION_TYPE_BUY,
        quantity=1,
        order_type=kite.ORDER_TYPE_MARKET,
        product=kite.PRODUCT_MIS
    )
    return order_id


# Place a market sell order function
def place_market_sell_order(kite, symbol, exchange):
    order_id = place_order(
        kite=kite,
        variety=kite.VARIETY_REGULAR,
        exchange=exchange,
        tradingsymbol=symbol,
        transaction_type=kite.TRANSACTION_TYPE_SELL,
        quantity=1,
        order_type=kite.ORDER_TYPE_MARKET,
        product=kite.PRODUCT_MIS
    )
    return order_id


# Get the latest market data and calculate the premium
# Main trading logic
def execute_trading_strategy(kite, symbol, target=0.45,
                             stop_loss=0.15,
                             trail_stop_loss_increment=0.9,
                             trail_stop_loss_enabled=True,
                             exchange='NSE'):
    initial_premium = get_latest_premium(kite, symbol, exchange)

    print(f"Buying {symbol} at the current price: {initial_premium}")
    #buy_order_id = place_market_buy_order(kite, symbol, exchange)
    #print(f"Buy order placed. Order ID: {buy_order_id}")

    # Wait for the buy order to be executed
    time.sleep(5)

    #if get_order_status(kite, orderId=buy_order_id) == 'COMPLETE':
    if True:
        print("Buy order executed successfully.")

        stop_loss_price = initial_premium - stop_loss
        target_price = initial_premium + target

        print(f"Stop loss price for {symbol}: {stop_loss_price}")
        print(f"Target loss price for {symbol}: {target_price}")

        while True:
            current_premium = get_latest_premium(kite, symbol, exchange)
            print(f"Current price of {symbol} is {current_premium}")

            if current_premium <= stop_loss_price:
                print(f"Stop loss triggered! for {symbol} Selling the stock...")
                #sell_order_id = place_market_sell_order(kite, symbol, exchange)
                #print(f"Sell order placed. Order ID: {sell_order_id}")
                break

            if current_premium >= target_price:
                print(f"Target achieved! for {symbol} Selling the stock...")
                #sell_order_id = place_market_sell_order(kite,symbol,exchange)
                #print(f"Sell order placed. Order ID: {sell_order_id}")
                break

            if current_premium >= initial_premium + trail_stop_loss_increment and trail_stop_loss_enabled:
                stop_loss_price = current_premium - stop_loss
                print(f"Stop loss price for {symbol} is now {stop_loss_price}")

            time.sleep(5)  # Pause for 5 second before checking again
