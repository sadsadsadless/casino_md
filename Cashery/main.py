import flask

class CashRegister:
    def __init__(self):
        self.rate = 10

    def moneyToChips(self, guestMoney):
        return {"chipsGiven": guestMoney * self.rate, "moneyRefund": 0}

    def chipsToMoney(self, guestChips):
        return {"moneyGiven": int(guestChips / self.rate), "chipsRefund": guestChips % self.rate}

if __name__ == "__main__":
    app = flask.Flask("cashRegister")
    CR = CashRegister()

    @app.route("/moneyToChips")
    def moneyToChips():
        money = int(flask.request.args.get("money", 0))
        toRet = CR.moneyToChips(money)
        print(f'gave {toRet["chipsGiven"]} chips for {money} money')
        return toRet

    @app.route("/chipsToMoney")
    def chipsToMoney():
        chips = int(flask.request.args.get("chips", 0))
        toRet = CR.chipsToMoney(chips)
        print(f'gave {toRet["moneyGiven"]} money for {chips} chips')
        return toRet

    app.run(port=5002)
