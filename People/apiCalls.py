import requests
import json

barUrl = '127.0.0.1:5000'
cashUrl = '127.0.0.1:5002'
tableUrl = '127.0.0.1:5007'

def money_to_chips(moneyAmountToExchange):
    while True:
        data = requests.get(f'http://{cashUrl}/moneyToChips?money={moneyAmountToExchange}')
        # print(f'money_to_chips: {len(data.text)}')
        # print(f'money_to_chips_bool: {bool(data.text)}')
        result = json.loads(data.text)
        if result:
            return result

def chips_to_money(chipsAmountToExchange):
    while True:
        data = requests.get(f'http://{cashUrl}/chipsToMoney?chips={chipsAmountToExchange}')
        # print(f'chips_to_money: {len(data.text)}')
        # print(f'chips_to_money_bool: {bool(data.text)}')
        result = json.loads(data.text)
        if result:
            return result

def get_alco_list():
    data = requests.get(f'http://{barUrl}/get_price_list')
    # print(f'get_alco_list: {len(data.text)}')
    alcoList = json.loads(data.text)
    return alcoList

def order_drink(name, amount, money):
    data = requests.get(f'http://{barUrl}/get_drink?name={name}&amount={amount}&money={money}')
    # print(f'order_drink: {len(data.text)}')
    alcoList = json.loads(data.text)
    return alcoList

def sit_at_place(table, place):
    data = requests.get(f'http://{tableUrl}/sit_at_place?table={table}&place={place}')
    # print(f'sit_at_place: {len(data.text)}')
    depo = int('0' + data.text)
    return depo

def try_play(table, place, name, money):
    data = requests.get(f'http://{tableUrl}/try_play?table={table}&money={money}&name={name}&place={place}')
    # print(f'try_play: {len(data.text)}')
    result = bool(int('0' + data.text))
    return result

def unlock_place(table, place):
    requests.get(f'http://{tableUrl}/unlock_table?table={table}&place={place}')

def get_free_spaces():
    while True:
        data = requests.get(f'http://{tableUrl}/get_free_spaces')
        # print(f'chips_to_money: {len(data.text)}')
        # print(f'chips_to_money code: {data.status_code}')
        if (data.text != '') and (data.text != []):
            return json.loads(data.text).get('places', [])
