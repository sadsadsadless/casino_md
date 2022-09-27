import random
import apiCalls as API

free = "free"


class Table:
    def __init__(
            self,
            tableType
    ):
        self.currentWinnings = 0
        if tableType == 'poker':
            self.places = [free,free,free,free]
            self.playTime = 100
            self.deposit = 100
            self.winChance = 0.40
            return
        if tableType == 'roulette':
            self.places = [free,free,free,free,free,free]
            self.playTime = 10
            self.deposit = 50
            self.winChance = 0.45
            return
        if tableType == 'one_armed_bandit':
            self.places = [free]
            self.playTime = 5
            self.deposit = 10
            self.winChance = 0.01
            return
        print(f'there is no tables with type {tableType}')

    def trySit(
            self,
            place
    ):
        if self.places[place] != free:
            return 0
        return self.deposit

    def tryPlay(
            self,
            place,
            money,
            player
    ):
        if money == self.deposit:
            self.currentWinnings += money
            self.places[place] = player
            readyToPlay = True
            for place in self.places:
                if place == free:
                    readyToPlay = False
                    break
            if readyToPlay:
                self._doGame()
            return True
        return False

    def _doGame(
            self
    ):
        time = self.playTime * 1000


        for person in self.places:
            if random.random() < self.winChance:
                money = self.deposit * 2
                self.currentWinnings -= money
            else:
                money = 0
            print(f'>>> time: {time}')
            API.sendGameResults(person, money, time)





