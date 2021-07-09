import json
from pprint import pprint
from firebase import firebase
import requests
import yfinance as yf

class Price:
    def __init__(self):
        pass
final_coin = []

firebase = firebase.FirebaseApplication('https://python-cryptoapp-default-rtdb.firebaseio.com/')
all_binance_coins = requests.get("https://api.binance.com/api/v3/ticker/24hr")
pendiente = json.loads(all_binance_coins.text)

def filter_data(pendiente, buscador):
    def iterator_func(x):
        for v in x.values():
            if buscador in v:
                return True
        return False
    return filter(iterator_func, pendiente)

for x in pendiente:
    x.pop('count')
    x.pop('firstId')
    x.pop('lastId')
    x.pop('closeTime')
    x.pop('openTime')

#CRIPTOMONEDAS FILTRADAS

final_coin.extend(list(filter_data(pendiente, 'BTCUSDT')))
final_coin.extend(list(filter_data(pendiente, 'ETHUSDT')))
final_coin.extend(list(filter_data(pendiente, 'BNBUSDT')))
final_coin.extend(list(filter_data(pendiente, 'ADAUSDT')))
final_coin.extend(list(filter_data(pendiente, 'DOGEUSDT')))
final_coin.extend(list(filter_data(pendiente, 'XRPUSDT')))
final_coin.extend(list(filter_data(pendiente, 'DOTUSDT')))
final_coin.extend(list(filter_data(pendiente, 'UNIUSDT')))
final_coin.extend(list(filter_data(pendiente, 'BHCUSDT')))
final_coin.extend(list(filter_data(pendiente, 'LTCUSDT')))
final_coin.extend(list(filter_data(pendiente, 'SOLUSDT')))
final_coin.extend(list(filter_data(pendiente, 'LINKUSDT')))
final_coin.extend(list(filter_data(pendiente, 'MATICUSDT')))
final_coin.extend(list(filter_data(pendiente, 'THETAUSDT')))
final_coin.extend(list(filter_data(pendiente, 'WBTCUSDT')))
final_coin.extend(list(filter_data(pendiente, 'ICPUSDT')))
final_coin.extend(list(filter_data(pendiente, 'XLMUSDT')))
final_coin.extend(list(filter_data(pendiente, 'ETCUSDT')))
final_coin.extend(list(filter_data(pendiente, 'VETUSDT')))
final_coin.extend(list(filter_data(pendiente, 'TRXUSDT')))
final_coin.extend(list(filter_data(pendiente, 'FILUSDT')))
final_coin.extend(list(filter_data(pendiente, 'XRMUSDT')))
final_coin.extend(list(filter_data(pendiente, 'EOSUSDT')))
final_coin.extend(list(filter_data(pendiente, 'SHIBUSDT')))
final_coin.extend(list(filter_data(pendiente, 'AAVEUSDT')))
final_coin.extend(list(filter_data(pendiente, 'BSVUSDT')))
final_coin.extend(list(filter_data(pendiente, 'CROUSDT')))
final_coin.extend(list(filter_data(pendiente, 'ALGOUSDT')))
final_coin.extend(list(filter_data(pendiente, 'KLAYUSDT')))
final_coin.extend(list(filter_data(pendiente, 'CAKEUSDT')))
final_coin.extend(list(filter_data(pendiente, 'AMPUSDT')))
final_coin.extend(list(filter_data(pendiente, 'FTTUSDT')))
final_coin.extend(list(filter_data(pendiente, 'NEOUSDT')))
final_coin.extend(list(filter_data(pendiente, 'XTZUSDT')))
final_coin.extend(list(filter_data(pendiente, 'LUNAUSDT')))
final_coin.extend(list(filter_data(pendiente, 'ATOMUSDT')))
final_coin.extend(list(filter_data(pendiente, 'MIOTAUSDT')))
final_coin.extend(list(filter_data(pendiente, 'LEOUSDT')))
final_coin.extend(list(filter_data(pendiente, 'TFUELUSDT')))
final_coin.extend(list(filter_data(pendiente, 'KSMUSDT')))
final_coin.extend(list(filter_data(pendiente, 'AVAXUSDT')))
final_coin.extend(list(filter_data(pendiente, 'HTUSDT')))
final_coin.extend(list(filter_data(pendiente, 'BTTUSDT')))
final_coin.extend(list(filter_data(pendiente, 'DCRUSDT')))
final_coin.extend(list(filter_data(pendiente, 'GRTUSDT')))
final_coin.extend(list(filter_data(pendiente, 'WAVESUSDT')))
final_coin.extend(list(filter_data(pendiente, 'CHZUSDT')))
final_coin.extend(list(filter_data(pendiente, 'ZCASHUSDT')))
final_coin.extend(list(filter_data(pendiente, 'HOTUSDT')))
final_coin.extend(list(filter_data(pendiente, 'SUSHIUSDT')))
final_coin.extend(list(filter_data(pendiente, 'ENJUSDT')))
final_coin.extend(list(filter_data(pendiente, 'MDXUSDT')))
final_coin.extend(list(filter_data(pendiente, 'DGBUSDT')))
final_coin.extend(list(filter_data(pendiente, 'OKBUSDT')))
final_coin.extend(list(filter_data(pendiente, 'SCUSDT')))
final_coin.extend(list(filter_data(pendiente, 'RVNUSDT')))
final_coin.extend(list(filter_data(pendiente, 'BAKEUSDT')))
final_coin.extend(list(filter_data(pendiente, '1INCHUSDT')))
final_coin.extend(list(filter_data(pendiente, 'IOSTUSDT')))
final_coin.extend(list(filter_data(pendiente, 'WINUSDT')))
final_coin.extend(list(filter_data(pendiente, 'WAXUSDT')))

with open("price.txt", "w+", encoding="utf-8") as f:
    for x in final_coin:
        f.write(str(x))
        f.write("\n")

resultado = firebase.post('/CRIPTOMONEDAS', final_coin)

if resultado:
    print('Datos Cargados')
else:
    print('Datos no cargados')

