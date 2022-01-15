from django.shortcuts import render, redirect
from django.http import HttpResponse
from tradingview_ta import TA_Handler, Interval, Exchange
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import ccxt
import random
from uniswap import Uniswap
from web3 import Web3

# from django.contrib.auth import get_user_model

# Create your views here.
def index(request): 
    if request.method == 'POST':
        exchangeSelected = request.POST['exchange']
        if(exchangeSelected != '--'):
            tickers = []
            if(exchangeSelected == 'WazirX'):
                tickers = getTickersWazir('WazirX')
            if(exchangeSelected == 'Binance'):
                tickers = getTickersBinance()
            if(exchangeSelected == 'Uniswap'):
                from .uniswap import currencies
                for a, b in currencies.items():
                    tickers.append(a)
            return render(request, 'components/exchangeTickers.html', {"tickers":tickers, "exchange":exchangeSelected })
        else:
            return HttpResponse("Please select an exchange.")
        
    content = {}   
    user_email = request.user.username
    content = get_exchanges(user_email) 
    # ticker = {}
    # if(dict_exchanges['WazirX']):
    #     ticker['WazirX'] = getTickersWazir('WazirX')
    #     content['WazirX'] = ticker['WazirX']
    # if(dict_exchanges['Binance']):
    #     ticker['Binance'] = getTickersBinance()
    #     content['Binance'] = ticker['Binance']
    # print(content)
    
    return render(request, 'index.html', {"content":content})

# def index(request, exchange): 
#     content = {}   
#     user_email = request.user.username
#     dict_exchanges = get_exchanges(user_email) 
#     ticker = {}
#     if(dict_exchanges['WazirX']):
#         ticker['WazirX'] = getTickersWazir('WazirX')
#         content['WazirX'] = ticker['WazirX']
#     if(dict_exchanges['Binance']):
#         ticker['Binance'] = getTickersBinance()
#         content['Binance'] = ticker['Binance']
#     print(content)
    
#     return render(request, 'index.html', {"content":content})
    
def markets(request):
    return render(request, 'markets.html')


def trade(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        exchange = request.POST['exchange']
        content = {}
        user_email = request.user.username
        content = getPriceAcrossExchanges(ticker,exchange, user_email)
        print(content)
        content["exchanges_available"] = get_exchanges(user_email)
    return render(request, 'components/technicalAnalysis.html', {"content":content})

def exchangeList(request):
    return render(request, 'exchangeList.html')

def credentialsAPI(request, exchange_name):
    if request.method == 'POST':
        apiKey = request.POST['apikey']
        apiSecretkey = request.POST['apiSecretkey']
        accountLabel = request.POST['accountLabel']
        current_user = request.user
        userPresent = UserApi.objects.all().filter(email=current_user.username)
        if(len(userPresent) == 1):
            if(accountLabel == "Binance"):
                UserApi.objects.filter(email=current_user.username).update(binanceApi=apiKey, binanceSecret = apiSecretkey)
                return render(request, 'credentialsAPI.html', {"success": True, "exchange_name": accountLabel})
            if(accountLabel == "WazirX"):
                UserApi.objects.filter(email=current_user.username).update(wazirApi=apiKey, wazirSecret = apiSecretkey)
                return render(request, 'credentialsAPI.html', {"success": True, "exchange_name": accountLabel})
            if(accountLabel == "Uniswap"):
                UserApi.objects.filter(email=current_user.username).update(uniswapPublic=apiKey, uniswapPrivate = apiSecretkey)
                return render(request, 'credentialsAPI.html', {"success": True, "exchange_name": accountLabel})
        else:
            if(accountLabel == "Binance"):
                single_userapi = UserApi(email = current_user.username, binanceApi=apiKey, binanceSecret = apiSecretkey )
                single_userapi.save()
                return render(request, 'credentialsAPI.html', {"success": True, "exchange_name": accountLabel})
            if(accountLabel == "WazirX"):
                single_userapi = UserApi(email = current_user.username, wazirApi=apiKey, wazirSecret = apiSecretkey )
                single_userapi.save()
                return render(request, 'credentialsAPI.html', {"success": True, "exchange_name": accountLabel})
            if(accountLabel == "Uniswap"):
                single_userapi = UserApi(email = current_user.username, uniswapPublic=apiKey, uniswapPrivate = apiSecretkey )
                single_userapi.save()
                return render(request, 'credentialsAPI.html', {"success": True, "exchange_name": accountLabel})


    arr = ["Binance", "WazirX", "Uniswap"]
    if exchange_name in arr:
        return render(request, 'credentialsAPI.html', {"exchange_name": exchange_name})
    return HttpResponse("This page doesn't exist.")

def portfolio(request):
    content ={
        "Binance" : False,
        "WazirX" : False,
        "Uniswap" : False,
        "error" : True,
        "error_msg" : "No API keys present. Please connect to your preferred exchanges by clicking 'Exchanges' in navbar."
    }
    user_email = request.user.username
    userapi = UserApi.objects.all().filter(email=user_email)
    if(len(userapi)== 1):
        i=0
        if(userapi[0].wazirApi and userapi[0].wazirSecret):
            content['WazirX'] = True
            content["wazirxBalance"] = getBalanceWazir(userapi[0].wazirApi, userapi[0].wazirSecret , 'WazirX')
            i=i+1
        if(userapi[0].binanceApi and userapi[0].binanceSecret):
            content['Binance'] = True            
            content["binanceBalance"] = getBalanceBinance(userapi[0].binanceApi, userapi[0].binanceSecret , 'Binance')
            i=i+1
        if(userapi[0].uniswapPublic):
            content['Uniswap'] = True            
            content["uniswapBalance"] = getBalanceUniswap(userapi[0].uniswapPublic)
            i=i+1
        if(i>0):
            content['error'] = False
            content['error_msg'] = ''
    
    return render(request, 'portfolio.html',content )

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context={'form' : form}
    return render(request, 'registration/signup.html', context)


def getBalanceWazir(api, secret, exchange):
    if(exchange == 'WazirX'):
        wazirx = ccxt.wazirx({
        'rateLimit': 10000,
        'apiKey': api,
        'secret': secret,
        })
        balances = wazirx.fetch_balance()

    filteredBalance = {}
    color = ['red', 'yellow', 'green', 'rgba(161, 6, 86, 0.8)', 'rgba(47, 107, 217, 0.8)', 'rgba(188, 244, 21, 0.8)', 'rgba(249, 164, 22, 0.8)', 'rgba(235, 80, 102, 0.8)', 'rgba(125, 235, 80, 0.8)', 'rgba(26, 116, 134, 0.8)', 'rgba(28, 91, 229, 0.8)', 'rgba(13, 47, 123, 0.91)', 'rgba(221, 28, 60, 0.91)']
    for x in balances:
        if(x == 'free' or x == 'total' or x == 'used'):
            continue
        else:
            if(balances[x]['total'] == 0.0):
                continue
            else:
                filteredBalance[x] = balances[x]
                if(exchange == 'WazirX'):
                    if (x == 'INR'):
                        filteredBalance[x]['price'] = balances[x]['total']
                        ran = random.randrange(0, len(color))
                        filteredBalance[x]['color'] = color[ran]
                    else:
                        filteredBalance[x]['price'] = wazirx.fetchTicker(x+"/INR")['close']*balances[x]['total']
                        ran = random.randrange(0, len(color))
                        filteredBalance[x]['color'] = color[ran]
                    print(filteredBalance)
    return filteredBalance
        
def getBalanceBinance(api, secret, exchange):
    
    if(exchange == 'Binance'):
        binance = ccxt.binance({
        'apiKey': api,
        'secret': secret,
        })
        markets = binance.fetchBalance()['info']['balances']

    filteredBalance = {}
    color = ['red', 'yellow', 'green', 'rgba(161, 6, 86, 0.8)', 'rgba(47, 107, 217, 0.8)', 'rgba(188, 244, 21, 0.8)', 'rgba(249, 164, 22, 0.8)', 'rgba(235, 80, 102, 0.8)', 'rgba(125, 235, 80, 0.8)', 'rgba(26, 116, 134, 0.8)', 'rgba(28, 91, 229, 0.8)', 'rgba(13, 47, 123, 0.91)', 'rgba(221, 28, 60, 0.91)']

    for index, market in enumerate(markets):
        amount = float(markets[index]['free']) + float(markets[index]['locked'])
        x = market['asset']
        
        if(amount != 0.0):
            filteredBalance[x] = market
            if(market['asset'] != 'USDT'):
                filteredBalance[x]['price'] = binance.fetchTicker(x+"/USDT")['close']*amount
                ran = random.randrange(0, len(color))
                filteredBalance[x]['color'] = color[ran]
            elif(markets[index]['asset'] == 'USDT'):
                filteredBalance[x]['price'] = amount
                ran = random.randrange(0, len(color))
                filteredBalance[x]['color'] = color[ran]
    
    print(filteredBalance)
    return filteredBalance


        
def getMarkets():

   
    return 0
        

def get_exchanges(email):
    content ={
        "Binance" : False,
        "WazirX" : False,
        "Uniswap" : False,
        "error" : True,
        "error_msg" : "No API keys present. Please connect to your preferred exchanges by clicking 'Exchanges' in navbar to trade."
    }
    userapi = UserApi.objects.all().filter(email=email)
    if(len(userapi)== 1):
        i=0
        if(userapi[0].wazirApi and userapi[0].wazirSecret):
            content['WazirX'] = True
            i=i+1
        if(userapi[0].binanceApi and userapi[0].binanceSecret):
            content['Binance'] = True            
            i=i+1
        if(userapi[0].uniswapPublic and userapi[0].uniswapPrivate):
            content['Uniswap'] = True            
            i=i+1
        if(i>0):
            content['error'] = False
            content['error_msg'] = False
    
    return content

def getTickersWazir(exchange):
    if(exchange == 'WazirX'):
        exchange_name = ccxt.wazirx({'rateLimit': 10000,})
    markets = exchange_name.fetchTickers()
    print(markets)
    all_tickers = []
    for market in markets:
        if(market[-4:] == 'USDT' or market[-3:] == 'INR' or market[-3:] == 'USD'):
            all_tickers.append(market)
            print(market)
    return all_tickers

def getTickersBinance():
    # binance
    binance = ccxt.binance()
    markets = binance.fetchTickers()
    all_tickers=[]
    for market in markets:
        if(market[-4:] == 'USDT' or market[-3:] == 'INR' or market[-3:] == 'USD'):
            all_tickers.append(market)
            print(market)
    return all_tickers


def getBalanceUniswap(publickey):
    # initializing uniswap
    address = publickey        
    private_key = ""  
    version = 3       
    provider = "https://mainnet.infura.io/v3/e0278c1f66e14692841c8a49796fda16"    # can also be set through the environment variable `PROVIDER`
    uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)
    from .uniswap import currencies

    filteredBalance = {}
    for currency, address in currencies.items():
        chk_sum = Web3.toChecksumAddress(address) 
        balance = uniswap.get_token_balance(chk_sum)
        if(balance != 0):
            filteredBalance[currency] = {"balance" : balance}
            # to get decimal places
            token = uniswap.get_token(chk_sum, 'erc20')
            strg = str(token)[6:-1]
            arr = strg.split(',')
            decimal = int(arr[2].strip())
            # to get price of that token in usdc
            price = uniswap.get_price_input(chk_sum, currencies["USDC"], 10**decimal)*balance
            filteredBalance[currency]['price'] = price
    return filteredBalance




def getPriceAcrossExchanges(ticker,exchange, user_email):
    content ={}
    # making connection with wazirX & binance
    wazirx = ccxt.wazirx()
    binance = ccxt.binance()

    hasSlash = ticker.find('/')
    if(hasSlash != -1):
        usdt_ticker = ticker.split('/')[0] + "/USDT"
        uniswap_ticker = ticker.split('/')[0]
    else:
        usdt_ticker = ticker + "/USDT"
        uniswap_ticker = ticker
    exchanges = get_exchanges(user_email)
    if(exchanges['WazirX']):
        try:
            content['WazirX'] = [wazirx.fetchTicker(usdt_ticker)['close'], usdt_ticker]
        except:
            content['WazirX'] = ["Could not find data for this symbol on WazirX", usdt_ticker]
    if(exchanges['Binance']):
        try:
            content['Binance'] = [binance.fetchTicker(usdt_ticker)['close'], usdt_ticker]
        except:
            content['Binance'] = ["Could not find data for this symbol on Binance", usdt_ticker]
    if(exchanges['Uniswap']):
        content['Uniswap'] = [getPriceUniswap(uniswap_ticker, "USDT"), usdt_ticker]

    # price of original ticker in original exchange

    if(exchange == "WazirX"):
        content["originalExchange"] = "WazirX"   
        content["originalPrice"] = wazirx.fetchTicker(ticker)['close']
    elif(exchange == "Binance"):
        content["originalExchange"] = "Binance"    
        content["originalPrice"] = binance.fetchTicker(ticker)['close']
    elif(exchange == "Uniswap"):
        content["originalExchange"] = "Uniswap"
        content["originalPrice"] =  getPriceUniswap(ticker, "USDT")
        
    content["originalTicker"] = ticker
    return content



def getPriceUniswap(coin, inTermsOf):
     # initializing uniswap
    address = ""        
    private_key = ""  
    version = 3       
    provider = "https://mainnet.infura.io/v3/e0278c1f66e14692841c8a49796fda16"    # can also be set through the environment variable `PROVIDER`
    uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)
    from .uniswap import currencies

    try:
        chk_sum = Web3.toChecksumAddress(currencies[coin]) 
        # to get decimal places for coin
        token1 = uniswap.get_token(chk_sum, 'erc20')
        strg = str(token1)[6:-1]
        arr = strg.split(',')
        decimal = int(arr[2].strip())
        # to get decimal places for intermsof
        token2 = uniswap.get_token(currencies[inTermsOf], 'erc20')
        strg2 = str(token2)[6:-1]
        arr2 = strg2.split(',')
        decimal2 = int(arr2[2].strip())
        # to get price of that token in usdc
        price = float(uniswap.get_price_input(chk_sum, currencies[inTermsOf], 10**decimal))/10**decimal2
    except Exception as e:
        price = "Not found on Uniswap"

    return price

def checkout(request):
    if request.method == 'POST':
        exchange = request.POST['exchange']
        orderType = request.POST['orderType']
        price = request.POST['price']
        amount = request.POST['amount']
        symbol = request.POST['symbol']
        buyOrSell = request.POST['buyOrSell']
        user = request.user.username
        userapi = UserApi.objects.all().filter(email=user)
        order = ""  
        if(buyOrSell == "Buy"):
            if(exchange == "WazirX"):
                wazirx = ccxt.wazirx({
                   'apiKey': userapi[0].wazirApi,
                   'secret': userapi[0].wazirSecret, 
                })
                if(orderType == "Limit"):
                    try: 
                        order = wazirx.createLimitBuyOrder(symbol, amount, price)
                    except Exception as e:
                        return HttpResponse(e)
                else:
                    try:
                        order = wazirx.createMarketBuyOrder(symbol, amount)
                    except Exception as e:
                        return HttpResponse(e)

            if(exchange == "Binance"):
                binance = ccxt.binance({
                   'apiKey': userapi[0].binanceApi,
                   'secret': userapi[0].binanceSecret, 
                })
                if(orderType == "Limit"):
                    try:
                        order = binance.createLimitBuyOrder(symbol, amount, price)
                    except Exception as e:
                        return HttpResponse(e)
                else:
                    try:
                        order = binance.createMarketBuyOrder(symbol, amount)
                    except Exception as e:
                        return HttpResponse(e)

            if(exchange == "Uniswap"):
                order = orderOnUniswap(userapi[0].uniswapPublic, userapi[0].uniswapPrivate, symbol, amount, buyOrSell)
        
        if(buyOrSell == "Sell"):
            if(exchange == "WazirX"):
                wazirx = ccxt.wazirx({
                   'apiKey': userapi[0].wazirApi,
                   'secret': userapi[0].wazirSecret, 
                })
                if(orderType == "Limit"):
                    try:
                        order = wazirx.createLimitSellOrder(symbol, amount, price)
                    except Exception as e:
                        return HttpResponse(e)
                else:
                    try:
                        order = wazirx.createMarketSellOrder(symbol, amount)
                    except Exception as e:
                        return HttpResponse(e)

            if(exchange == "Binance"):
                binance = ccxt.binance({
                   'apiKey': userapi[0].binanceApi,
                   'secret': userapi[0].binanceSecret, 
                })
                if(orderType == "Limit"):
                    try:
                        order = binance.createLimitSellOrder(symbol, amount, price)
                    except Exception as e:
                        return HttpResponse(e)
                else:
                    try:
                        order = binance.createMarketSellOrder(symbol, amount)
                    except Exception as e:
                        return HttpResponse(e)

            if(exchange == "Uniswap"):
                order = orderOnUniswap(userapi[0].uniswapPublic, userapi[0].uniswapPrivate, symbol, amount, buyOrSell)

    return render(request, "checkout.html")

def orderOnUniswap(pubKey, privateKey, symbol, amount, buyOrSell):
    address = pubKey        
    private_key = privateKey  
    version = 3       
    provider = "https://mainnet.infura.io/v3/e0278c1f66e14692841c8a49796fda16"    # can also be set through the environment variable `PROVIDER`
    uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)
    from .uniswap import currencies

    # get coin pair
    coin =""
    inTermsOf = ""
    hasSlash = symbol.find('/')
    if(hasSlash != -1):
        coin = symbol.split('/')[0]
        inTermsOf = symbol.split('/')[1]
    else:
        coin = symbol
        inTermsOf = "USDT"

    # get number of decimals
    chk_sum1 = Web3.toChecksumAddress(currencies[coin]) 
    chk_sum2 = Web3.toChecksumAddress(currencies[inTermsOf]) 
    token1 = uniswap.get_token(chk_sum1, 'erc20')
    token2 = uniswap.get_token(chk_sum2, 'erc20')
    strg1 = str(token1)[6:-1]
    strg2 = str(token2)[6:-1]
    arr1 = strg1.split(',')
    arr2 = strg2.split(',')
    decimal1 = int(arr1[2].strip())
    decimal2 = int(arr2[2].strip())

    # to get price of that token in usdc
    

    if(buyOrSell == "Buy"):
        try:
            price = uniswap.get_price_input(chk_sum1, currencies[inTermsOf], 10**decimal1)
            print(price)
            # amount_to_sell =price*amount
            # print(amount_to_sell)
            order = uniswap.make_trade(chk_sum2, chk_sum1, 10**decimal1)  # sell 1 ETH for BAT
        except Exception as e:
            return HttpResponse(e)
    else:
        try:
            order = uniswap.make_trade_output(chk_sum2, chk_sum1, amount**decimal1)  # buy ETH for 1 BAT
        except Exception as e:
            return HttpResponse(e)
    return order