# This is a sample Python script.
from classes.Stock import Stock
from commons.loginModule import login
from scripts.intradayUptrendAnalyserScript import getUptrendingStocksForNSE
from scripts.intradayBullishStocksAnalyserScript import getBullishStocksForNSE
from scripts.intradayStockMovementAnalyserScript import checkStockMovement
from indicators.bollingerBandTechnique import checkBollingerBandCondition
from indicators.supertrendTechnique import checkSupertrendCondition
from tradingScripts.tradingScript import execute_trading_strategy
import multiprocessing
from functools import partial

infyStock = Stock('INFY', 20, 10, 5)
vblStock = Stock('VBL', 25, 10, 5)
iobStock = Stock('IOB', 0.45, 0.15, 0.9)
iocStock = Stock('IOC', 0.55, 0.25, 0.9)
zomatoStock = Stock('ZOMATO', 0.55, 0.25, 0.9)
mahabankStock = Stock('MAHABANK', 0.45, 0.15, 0.9)

stockList = [iocStock, iobStock, zomatoStock, mahabankStock, infyStock, vblStock]
tradingSymbols = [obj.getSymbol() for obj in stockList]
tradingSymbolObjectMap = dict(zip(tradingSymbols, stockList))


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def checkMultipleConditionsAndExecuteScript(stockSymbol, kite, period, exchange):
    #checkBollingerBandCondition(kite, stockSymbol, period, exchange)
    checkSupertrendCondition(kite, stockSymbol, period, exchange)
    if checkStockMovement(kite, stockSymbol, period, exchange) == "Upwards":
        stockObject = tradingSymbolObjectMap.get(stockSymbol)
        execute_trading_strategy(kite=kite, symbol=stockSymbol, exchange=exchange,
                                 target=stockObject.getTarget(),
                                 stop_loss=stockObject.getStopLoss(),
                                 trail_stop_loss_increment=stockObject.getTrailStopLossIncrement())


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    api_key = "api_key"
    api_secret = "api_secret"
    kite = login(api_key, api_secret)


    # tradingSymbols = ['ZOMATO', 'MAHABANK', 'IOC', 'IOB']
    # tradingSymbols = ['ZEEL23JUNFUT', 'INFY23JUNFUT', 'TCS23JUNFUT']
    exchange = 'NSE'
    period = 15

    # Identify the upgoing stocks
    uptrendingStocksForNSESymbols = getUptrendingStocksForNSE(kite, tradingSymbols, period, exchange)

    bullishStocksForNSESymbol = getBullishStocksForNSE(kite, tradingSymbols, exchange)

    num_processes = len(uptrendingStocksForNSESymbols)

    if num_processes > 0:

        # Create a process pool with the specified number of processes
        pool = multiprocessing.Pool(processes=num_processes)

        # Create a partial function with the additional arguments bound
        partial_process_function = partial(checkMultipleConditionsAndExecuteScript, kite=kite, period=period,
                                           exchange=exchange)

        # Map the list elements to the process function and execute them in parallel
        pool.map(partial_process_function, uptrendingStocksForNSESymbols)

        # Close the process pool and wait for all processes to finish
        pool.close()
        pool.join()

    else:
        print("No stock is trending")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
