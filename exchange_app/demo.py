import ccxt
def func():
    exchange=ccxt.binance({
    'apiKey': "72WHUcB3FjNaEr63X1KpPvcGBbVHSltjGqx0O5Hzi0MS1DnrJcRreKYtkWrdS3O4",
    'secret': "ZNIL31GRLLukRBQBRvrWNChNtBdQwMjj0k9Ru8RkSxEGsLobEGTelICdczto2XUa",
    })
    
    if (exchange.has['fetchOpenOrders']):
        openOrderBinance = exchange.fetchOpenOrders(symbol = "SOL/USDT", limit = 30)
        # content["openOrderBinance"] = openOrderBinance
        # time.sleep(1)
        print(openOrderBinance)
    if (exchange.has['fetchClosedOrders']):
        closedOrderBinance = exchange.fetchClosedOrders(symbol = "SOL/USDT", limit = 20)
        # content["closedOrderBinance"] = closedOrderBinance
        # time.sleep(1)
        print(closedOrderBinance)