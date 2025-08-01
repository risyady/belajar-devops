import json

""" x = '{"name": "Risyad", "age": 21, "city": "Padang"}'

y = json.loads(x)

print(y["age"]) """

x = {
        "name": "Risyad",
        "age": 21,
        "city": "Padang"
    }

y = json.dumps(x, indent=4, sort_keys=True)

print(y)