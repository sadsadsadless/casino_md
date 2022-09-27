from random import choices, random
import threading
import os

import flask
import flask_cors

from person import Person

peopleAmount = 10

class Module:
    def __init__(
            self
    ):
        self.people = {}
        self.maxPeople = 50
        self.counter = 0

    def _generate_person(
            self
    ):
        with open(f"{os.path.dirname(__file__)}/names.txt", "r") as f:
            lines = f.readlines()
            name = choices(lines)[0][:-1]
        if name in self.people:
            name = f'{name}_{self.counter}'
        self.people[name] = (Person(name))
        self.counter += 1

    def generate_people(
            self,
            n=1
    ):
        for _ in range(n):
            self._generate_person()

    def remove_person(
            self,
            person
    ):
        self.people[person].state = 'left'

    def get_people_data(
            self
    ):
        return {'amount': len(self.people)}

    def get_people_list(
            self
    ):
        return [name for name in self.people if self.people[name].state != 'left']

    def get_person_info(
            self,
            personName
    ):
        if personName in self.people:
            return {
                'chips': self.people[personName].chips,
                'money': self.people[personName].money,
                'drunkness': self.people[personName].drunkness,
            }
        return {
            'chips': 0,
            'money': 0,
            'drunkness': 0,
        }

    def make_endgame(self, person, money):
        self.people[person].endGame(money)

    def step(
            self
    ):
        print('step in process')
        for person in list(self.people):
            if self.people[person].state == 'left':
                continue
            # print(f'{person}: {self.people[person].state}')
            if self.people[person].state == 'new':
                self.people[person].convertMoneyToChips()
            if self.people[person].state == 'idle':
                rnd = random()
                if (rnd < 0.1) or (self.people[person].chips <= 100):
                    self.people[person].state = 'leaving'
                elif (rnd > 0.9) and (self.people[person].drunkness <= 40):
                    self.people[person].drinkAlco()
                else:
                    self.people[person].playGame()
            if self.people[person].state == 'leaving':
                self.remove_person(person)
                self._generate_person()
        threading.Timer(1, lambda: self.step()).start()


if __name__ == '__main__':
    peopleModule = Module()
    peopleModule.generate_people(peopleAmount)

    app = flask.Flask('peopleModule')
    flask_cors.CORS(app)

    @app.route('/get_people_list')
    def get_people_list():
        return {'list': peopleModule.get_people_list()}

    @app.route('/get_person_info')
    def get_person_info():
        name = flask.request.args.get('name', 0)
        return peopleModule.get_person_info(name)

    @app.route('/person_end_game')
    def person_end_game():
        name = flask.request.args.get('name', '')
        money = int(flask.request.args.get('money', 0))
        time = int(flask.request.args.get('time', 0))
        threading.Timer(int(time / 1000), lambda: peopleModule.make_endgame(name, money)).start()
        return 'ok'


    threading.Timer(1, lambda: peopleModule.step()).start()

    app.run(port=5001)
