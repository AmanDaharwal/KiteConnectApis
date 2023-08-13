def get_order_status(kite, orderId):

    received = kite.orders()
    for individualOrders in received:

        if int(individualOrders['order_id']) == int(orderId):
            status = individualOrders['status']
            print("Order ID "+orderId+" is "+status)
            return status