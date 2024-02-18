from requests import get

API_KEY = ""
URL = "https://api.freecurrencyapi.com/"

def getcurrencies():
    attachment = f"v1/currencies?apikey={API_KEY}"
    url = URL + attachment
    data = get(url).json()['data']

    data = list(data.items())
    data.sort()
    return data

def currencyprinter(currencies):
    for abbreviation,currency in currencies:
        name = currency['name']
        symbol = currency['symbol_native']
        print(f"{name} - {abbreviation} - {symbol}")
    print() #to clear a line for later

def exchange(amount,currency1,currency2):
    attachment = f"v1/latest?apikey={API_KEY}&base_currency={currency1}"
    url = URL + attachment
    data = get(url).json()
    if data.get('data')==None:
        print("\033[31mInvalid currencies. Refer to the currency acronyms above,")
        getinput()
    else:
        data = data['data']
        print(f"\033[33m{amount} {currency1} is {float(amount)*data[f'{currency2}']} {currency2}")

def getinput():
    amount=input("\033[36mAmount of Currency ")
    currency1=input("\033[36mCurrency#1 ")
    currency2=input("\033[36mCurrency#2 ")
    exchange(amount,currency1.upper(),currency2.upper())

currencyprinter(getcurrencies())
getinput()
