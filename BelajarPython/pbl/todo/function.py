import json
import os

DB_FILE = "db.json"

if not os.path.exists("db.json"):
    with open(DB_FILE, 'w') as f:
        json.dump([], f)

def read_data():
    with open(DB_FILE) as f:
        return json.load(f)
    
def write_data(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def show_data():
    data = read_data()
    for item in data:
        print(item)

def create_data(_task):
    data = read_data()
    record = { 
        "id": uuid(data), 
        "task": _task, 
        "status": "Progress" 
    }
    data.append(record)
    write_data(data)
    print(record)

def uuid(data):
    ids = []
    new_id = 1
    [ids.append(x["id"]) for x in data]
    while new_id in ids:
        new_id += 1
    
    return new_id