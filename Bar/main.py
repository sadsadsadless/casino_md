import flask
import flask_cors

class Bar:
    def __init__(self):
        self.alco = {
            'Empty': {'price': 0, 'proof': 0, 'volume': 0},
            'Beer': {'price': 10, 'proof': 5.5, 'volume': 0.25},
            'Vodka': {'price': 8, 'proof': 40, 'volume': 0.25},
            'Rom': {'price': 12, 'proof': 42, 'volume': 0.25},
            'Wisky': {'price': 14, 'proof': 38, 'volume': 0.25},
            'Absinthe': {'price': 11, 'proof': 70, 'volume': 0.25},
            'Tequila': {'price': 14, 'proof': 70, 'volume': 0.25},
            'Cognac': {'price': 10, 'proof': 40, 'volume': 0.25},
            'Cola': {'price': 6, 'proof': 0, 'volume': 0.5},
            'Sprite': {'price': 6, 'proof': 0, 'volume': 0.5},
            'Fanta': {'price': 6, 'proof': 0, 'volume': 0.5},
            'Water': {'price': 6, 'proof': 0, 'volume': 0.5},
        }

    def get_price_list(self):
        return {i: self.alco[i] for i in self.alco if i != 'Empty'}

    def get_drink(self, name, amount, money):
        drink = self.alco.get(name, self.alco['Empty'])
        total_price = drink['price']*amount
        if total_price <= money:
            return {'amount': amount, 'moneyBack': money - total_price, 'proof': drink['proof']}
        else:
            bottles = int(money / drink['price'])
            return {'amount': bottles, 'moneyBack': money - bottles * drink['price'], 'proof': drink['proof']}


if __name__=='__main__':
    b = Bar()
    app = flask.Flask('bar')
    flask_cors.CORS(app)

    @app.route('/get_price_list')
    def get_price_list():
        print('offered a price-list')
        return b.get_price_list()

    @app.route('/get_drink')
    def get_drink():
        name = flask.request.args.get('name', 'Empty')
        amount = int(flask.request.args.get('amount', 0))
        money = int(flask.request.args.get('money', 0))
        print(f'giving {name} drink ({amount}) for {money} chips')
        return b.get_drink(name, amount, money)

    app.run(port=5000)

