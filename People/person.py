from random import choices
import apiCalls as API


charType = [
    ['normal', 100],
    ['lucky', 10],
    ['unlucky', 15],
    ['rich', 10],
    ['smart', 5]
]

class Person:
    def __init__(
            self,
            personName
    ):
        self.name = personName
        self.type = choices([per[0] for per in charType], weights=[per[1] for per in charType])[0]
        #self.money = choices([i for i in range(80, 120)])[0] if self.type != 'rich' else 10000
        self.money = 20 if self.type != 'rich' else 10000
        self.chips = 0
        self.state = 'new'
        self.statesChances = {
            'money_to_chips': 10,
            'chips_to_money': 0,
            'play_game': 0,
            'drink_alco': 0,
            'leave': 0
        }
        self.coords = {'x': 0, 'y': 0}
        self.drunkness = 0
        self.table = -1
        self.place = -1

    def convertMoneyToChips(
            self
    ):
        converted = API.money_to_chips(self.money)
        self.money = converted['moneyRefund']
        self.chips += converted['chipsGiven']
        self.state = 'idle'

    def convertChipsToMoney(
            self
    ):
        converted = API.chips_to_money(self.chips)
        self.money += converted['moneyGiven']
        self.chips = converted['chipsRefund']

    def playGame(
            self
    ):
        tablesList = API.get_free_spaces()
        table = choices(tablesList)[0]
        self._goto(table['x'], table['y'])
        isSit = API.sit_at_place(table['table'], table['place'])
        if isSit == 0:
            return
        depo = choices([10, 50, 100])[0]
        isPlay = API.try_play(table['table'], table['place'], self.name, depo)
        if isPlay:
            self.chips -= depo
            self.table = table['table']
            self.place = table['place']
            self.state = 'playing'
            return

    def endGame(
            self,
            chips
    ):
        self.chips += chips
        self.state = 'idle'
        API.unlock_place(self.table, self.place)
        self.table = -1
        self.place = -1

    def _goto(
            self,
            x,
            y
    ):  # todo()
        self.state = 'going'
        self.coords = {'x': x, 'y': y}
        self.state = 'idle'

    def drinkAlco(
            self
    ):
        alcoList = API.get_alco_list()
        alcoName = choices(list(alcoList.keys()))[0]
        amounts = [1, 2, 3] if self.drunkness < 10 else [1, 2] if self.drunkness < 20 else [1] if self.drunkness < 30 else [0]
        amount = choices(amounts)[0]
        price = alcoList[alcoName]['price'] * amount
        chips = min(price, self.chips)
        self.chips -= chips
        response = API.order_drink(name=alcoName, amount=amount, money=chips)
        self.chips += response['moneyBack']
        self.drunkness += response['amount'] * response['proof'] / 10



