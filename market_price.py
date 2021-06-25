import json
import requests
import time
from firebase import firebase


class Price:
    def __init__(self):
        pass

    count = 0
    count_1 = 1
    n_coins = 1528

    firebase = firebase.FirebaseApplication('https://python-cryptoapp-default-rtdb.firebaseio.com/')
    response = requests.get("https://api.binance.com/api/v3/ticker/price")
    pendiente = json.loads(response.text)
    prices = json.dumps(pendiente)

    with open("D:\Python Code\python_stock\price.json", "w", encoding="utf-8") as f:
        f.write(prices)

    with open("D:\Python Code\python_stock\price.txt", "w+", encoding="utf-8") as f:
        for price in pendiente:
            count = count + 1
            str_price = str(price)
            f.write(str_price)
            f.write("\n")

            if str_price[12:20] == 'CAKEUSDT':
                CAKEUSDT = str_price[12:20]
                price_CAKEUSDT = str_price[33:43]
                _price_CAKEUSDT = float(str_price[33:43])
                mapCAKEUSDT = {CAKEUSDT: _price_CAKEUSDT}

                #print("\n" + CAKEUSDT)
                #print('Precio: ' + price_CAKEUSDT)
                #print(mapCAKEUSDT)

            elif str_price[12:20] == 'CAKEBUSD':
                CAKEBUSD = str_price[12:20]
                price_CAKEBUSD = str_price[33:43]
                _price_CAKEBUSD = float(price_CAKEBUSD)
                mapCAKEBUSD = {CAKEBUSD: _price_CAKEBUSD}

                #print("\n" + CAKEBUSD)
                #print('Precio: ' + price_CAKEBUSD)

            if count == 1528:
                mapcriptomoneda = {}
                #mapcriptomoneda = mapCAKEUSDT, mapCAKEBUSD
                mapcriptomoneda.update(mapCAKEUSDT)
                mapcriptomoneda.update(mapCAKEBUSD)
                print('\nAPP Actualizada\n')
                print(mapcriptomoneda)

            elif count > 1528:
                print('Actualizar APP, Nueva Criptomoneda Añadida')

    resultado = firebase.post('/CRIPTOMONEDAS', mapcriptomoneda)
            # print(count)




