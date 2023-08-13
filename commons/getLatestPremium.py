def get_latest_premium(kite, symbol, exchange='NSE'):
    ltp_data = kite.ltp(exchange + ':' + symbol)
    ltp = ltp_data[exchange + ':' + symbol]['last_price']
    return ltp