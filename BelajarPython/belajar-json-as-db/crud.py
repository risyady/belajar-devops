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
    data.append(item)
    write_data(data)

if __name__ == '__main__':
    create_data({"id": "5", "name": "Rahmat"})
    show_data()