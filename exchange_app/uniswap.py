# from uniswap import Uniswap
# from web3 import Web3
currencies = {
        "ETH": "0x0000000000000000000000000000000000000000",
        "1INCH" : "0x111111111117dC0aa78b770fA6A738034120C302",
        "AAVE" : "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
        "AMP" : "0xfF20817765cB7f73d4bde2e66e067E58D11095C2",
        "ANT" : "0xa117000000f279D81A1D3cc75430fAA017FA5A2e",
        "BAL" : "0xba100000625a3754423978a60c9317c58a424e3D",
        "BAND" : "0xBA11D00c5f74255f56a5E366F4F77f5A186d7f55",
        "BAT" : "0x0D8775F648430679A709E98d2b0Cb6250d2887EF",
        "BNT" : "0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C",
        "COMP" : "0xc00e94Cb662C3520282E6f5717214004A7f26888",
        "CRV" : "0xD533a949740bb3306d119CC777fa900bA034cd52",
        "CVC" : "0x41e5560054824eA6B0732E656E3Ad64E20e94E45",
        "DAI" : '0x6b175474E89094C44Da98b954EedeAC495271d0F',
        "DNT" : "0x0AbdAce70D3790235af448C88547603b945604ea",
        "ENJ" : "0xF629cBd94d3791C9250152BD8dfBDF380E2a3B9c",
        "ENS" : "0xC18360217D8F7Ab5e7c516566761Ea12Ce7F9D72",
        "GNO" : "0x6810e776880C02933D47DB1b9fc05908e5386b96",
        "GRT" : "0xc944E90C64B2c07662A292be6244BDf05Cda44a7",
        "GUSD" : "0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd",
        "KEEP" : "0x85Eee30c52B0b379b046Fb0F85F4f3Dc3009aFEC",
        "KNC" : "0xdeFA4e8a7bcBA345F687a2f1456F5Edd9CE97202",
        "LINK" : '0x514910771AF9Ca656af840dff83E8264EcF986CA',
        "LOOM" : '0xA4e8C3Ec456107eA67d3075bF9e3DF3A75823DB0',
        "LRC" : '0xBBbbCA6A901c926F240b89EacB641d8Aec7AEafD',
        "MANA" : '0x0F5D2fB29fb7d3CFeE444a200298f468908cC942',
        "MATIC" : "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0",
        "MKR" : '0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2',
        "MLN" : "0xec67005c4E498Ec7f55E092bd1d35cbC47C91892",
        "NMR": "0x1776e1F26f98b1A5dF9cD347953a26dd3Cb46671",
        "NU": "0x4fE83213D56308330EC302a8BD641f1d0113A4Cc",
        "OXT" : "0x4575f41308EC1483f3d399aa9a2826d74Da13Deb",
        "PAXG" : "0x45804880De22913dAFE09f4980848ECE6EcbAf78",
        "REN" : "0x408e41876cCCDC0F92210600ef50372656052a38",
        "REP" : "0x1985365e9f78359a9B6AD760e32412f4a445E862",
        "SAND" : "0x3845badAde8e6dFF049820680d1F14bD3903a5d0",
        "SKL" : "0x00c83aeCC790e8a4453e5dD3B0B4b3680501a7A7",
        "SNX" : '0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F',
        "STORJ" : "0xB64ef51C888972c908CFacf59B47C1AfBC0Ab8aC",
        "SUSD" : "0x57Ab1ec28D129707052df4dF418D58a2D46d5f51",
        "TBTC" : "0x8dAEBADE922dF735c38C80C7eBD708Af50815fAa",
        "UMA" : "0x04Fa0d235C4abf4BcF4787aF4CF447DE572eF828",
        "UNI" : "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
        "USDC" : "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "USDT" : "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        "WBTC" : "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
        "WETH" : "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "YFI" : '0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e',
        "ZRX" : "0xE41d2489571d322189246DaFA5ebDe1F4699F498",
    }

# def f1():
#     address = "0x00000000219ab540356cBB839Cbe05303d7705Fa"          # or None if you're not going to make transactions
#     private_key = ""  # or None if you're not going to make transactions
#     version = 3                       # specify which version of Uniswap to use
#     provider = "https://mainnet.infura.io/v3/e0278c1f66e14692841c8a49796fda16"    # can also be set through the environment variable `PROVIDER`
#     uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

#     # Some token addresses we'll be using later in this guide
#     eth = "0x0000000000000000000000000000000000000000"
#     bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
#     dai = "0x6b175474E89094C44Da98b954EedeAC495271d0F"
#     weth = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
#     matic = "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0"
#     poly ="0x9992eC3cF6A55b00978cdDF2b27BC6882d88D1eC"

    

    # Returns the amount of DAI you get for 1 ETH (10^18 wei)
    # output = uniswap.get_price_input(eth, dai, 10**18)

    # Returns the amount of ETH you need to pay (in wei) to get 1000 DAI
    # output = uniswap.get_price_output(eth, dai, 1_000 * 10**18)

    # Get the balance of ETH for your address.
    # output = uniswap.get_eth_balance()

    # Get the balance of a token for your address.
    # chk_sum = Web3.toChecksumAddress('0x41e5560054824eA6B0732E656E3Ad64E20e94E45') 
    # print(chk_sum)
    # output = uniswap.get_token_balance(chk_sum)

    # Make a trade by specifying the quantity of the input token you wish to sell
    # uniswap.make_trade(eth, bat, 1*10**18)  # sell 1 ETH for BAT
    # uniswap.make_trade(bat, eth, 1*10**18)  # sell 1 BAT for ETH
    # uniswap.make_trade(bat, dai, 1*10**18)  # sell 1 BAT for DAI
    # uniswap.make_trade(eth, bat, 1*10**18, "0x123...")  # sell 1 ETH for BAT, and send the BAT to the provided address
    # uniswap.make_trade(dai, usdc, 1*10**18, fee=500)    # sell 1 DAI for USDC using the 0.05% fee pool (v3 only)

    # Make a trade by specifying the quantity of the output token you wish to buy
    # uniswap.make_trade_output(eth, bat, 1*10**18)  # buy ETH for 1 BAT
    # uniswap.make_trade_output(bat, eth, 1*10**18)  # buy BAT for 1 ETH
    # uniswap.make_trade_output(bat, dai, 1*10**18, "0x123...")  # buy BAT for 1 DAI, and send the BAT to the provided address
    # uniswap.make_trade_output(dai, usdc, 1*10**8, fee=500)     # buy USDC for 1 DAI using the 0.05% fee pool (v3 only)

    # for decimal
    # output = uniswap.get_token(chk_sum, 'erc20')
    # strg = str(output)[6:-1]
    # arr = strg.split(',')
    # decimal = arr[2].strip()
    # return 0