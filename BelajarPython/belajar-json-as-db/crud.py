import json
import os

# Kalau var yang dipakai itu tidak berubah/Konstanta gunakan huruf besar
DB_FILE = 'data.json'

if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w') as f:
        json.dump([], f)

def read_data():
    with open(DB_FILE) as f:
        return json.load(f)

def write_data(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def show_data():
    print(read_data())

def create_data(item):
    data = read_data()
    record = {
        "id": uuid(data),
        "task": item,
        "status": "Progress"
    }
    data.append(record)
    write_data(data)

def uuid(data):
    #data = read_data()
    #print(type(ids))
    ids = []
    new_id = 1
    [ids.append(x["id"]) for x in data]
    while new_id in ids:
        new_id += 1
    
    return new_id

if __name__ == '__main__':
    create_data("Belajar argparse")
    show_data()