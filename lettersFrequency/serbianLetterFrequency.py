import json

with open('serbianLetterFrequency.json') as f:
    data = json.load(f)


def get_serbian_dictionary():
    return data
