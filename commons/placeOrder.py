from kiteconnect import KiteConnect
from kiteconnect.exceptions import KiteException


# Function to place an order
def place_order(kite, tradingsymbol, exchange, transaction_type, quantity, order_type, variety, product, price=None):
    try:
        orderId = kite.place_order(
            tradingsymbol=tradingsymbol,
            exchange=exchange,
            transaction_type=transaction_type,
            quantity=quantity,
            order_type=order_type,
            product=product,
            variety=variety,
            price=price)
        return orderId
    except KiteException as e:
        print(f"ERROR : Order placement failed: { str(e)}")
        return None
