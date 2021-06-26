import json
import requests
import time
from firebase import firebase


def place(str_price, cripto):
    global mapcrypto
    numeros = []

    for x in range(0, 10):
        x_str = str(x)
        x_price = str_price.find(x_str)

        if x_price != -1 and x_price > 25:
            numeros.append(x_price)

        elif 0 < x_price < 25:  # Excepción para KP3RBNB
            f_price = str_price[32:41]  # Corregir

    s_price = min(numeros) + str_price[min(numeros):].find("'")
    f_price = str_price[min(numeros):s_price]

    mapcrypto = {'Symbol': cripto, 'Price': float(f_price)}

    # print("")
    # print(f_price)
    # print(mapcrypto)


mapcrypto = {}


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
        list_criptomoneda = []

        for price in pendiente:
            count = count + 1
            str_price = str(price)
            f.write(str_price)
            f.write("\n")

            if str_price[17] == "'":
                cripto = str_price[12:17]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                #print('5: ' + cripto)

            elif str_price[18] == "'":
                cripto = str_price[12:18]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                # print('5: ' + cripto)

            elif str_price[19] == "'":
                cripto = str_price[12:19]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                # print('5: ' + cripto)

            elif str_price[20] == "'":
                cripto = str_price[12:20]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                # print('5: ' + cripto)

            elif str_price[21] == "'":
                cripto = str_price[12:21]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                # print('5: ' + cripto)

            elif str_price[22] == "'":
                cripto = str_price[12:22]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                # print('5: ' + cripto)

            elif str_price[23] == "'":
                cripto = str_price[12:23]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                # print('5: ' + cripto)

            elif str_price[24] == "'":
                cripto = str_price[12:24]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                # print('5: ' + cripto)

            elif str_price[25] == "'":
                cripto = str_price[12:25]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                # print('5: ' + cripto)

            elif str_price[21] == "'":  # No existe cripto con más de 13 letras
                cripto = str_price[12:26]
                place(str_price, cripto)
                list_criptomoneda.append(mapcrypto)
                # print('5: ' + cripto)



            #if str_price[12:20] == 'CAKEUSDT':
                #CAKEUSDT = str_price[12:20]
                #price_CAKEUSDT = str_price[33:43]
                #_price_CAKEUSDT = float(str_price[33:43])

                # mapCAKEUSDT = {CAKEUSDT: _price_CAKEUSDT}

                # print("\n" + CAKEUSDT)
                # print('Precio: ' + price_CAKEUSDT)
                # print(mapCAKEUSDT)

            #elif str_price[12:20] == 'CAKEBUSD':
                #CAKEBUSD = str_price[12:20]
                #price_CAKEBUSD = str_price[33:43]
                #_price_CAKEBUSD = float(price_CAKEBUSD)
                #mapCAKEBUSD = {CAKEBUSD: _price_CAKEBUSD}

                # print("\n" + CAKEBUSD)
                # print('Precio: ' + price_CAKEBUSD)

            if count == 1528:

                # mapcriptomoneda = mapCAKEUSDT, mapCAKEBUSD
                # mapcriptomoneda.update(mapCAKEUSDT)
                # mapcriptomoneda.update(mapCAKEBUSD)
                print('\nAPP Actualizada\n')
                # print(mapcriptomoneda)

            elif count > 1528:
                print('Actualizar APP, Nueva Criptomoneda Añadida')

    #print(mapcriptomoneda)
    #print(list_criptomoneda)
    resultado = firebase.post('/CRIPTOMONEDAS', list_criptomoneda)

