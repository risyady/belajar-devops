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

def update_data(_id):
    data = read_data()
    item = [x for x in data if x["id"] == _id]
    if item[0] in data:
        data.remove(item[0])
    item[0]["status"] = "Done"
    data.append(item[0])
    write_data(data)
    print(item[0]["task"])

def remove_data(_id):
    data = read_data()
    item = [x for x in data if x["id"] == _id]
    if item[0] in data:
        data.remove(item[0])
    write_data(data)
    print(item[0]["task"])

def uuid(data):
    ids = []
    new_id = 1
    [ids.append(x["id"]) for x in data]
    while new_id in ids:
        new_id += 1
    
    return new_id