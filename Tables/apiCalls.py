import requests
import json

def sendGameResults(name, money, time):
    requests.get(f'http://127.0.0.1:5001/person_end_game?name={name}&money={money}&time={time}')