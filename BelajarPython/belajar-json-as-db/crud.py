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

def create_data(_task):
    data = read_data()
    record = {
        "id": uuid(data),
        "task": _task,
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

def update_data(_id):    
    datalist = read_data()
    data = [x for x in datalist if x["id"] == _id]
    datalist.remove(data[0])
    data[0]["status"] = "Done"
    datalist.append(data[0])
    write_data(datalist)

def remove_data(_id):
    datalist = read_data()
    data = [x for x in datalist if x["id"] == _id]
    datalist.remove(data[0])
    write_data(datalist)
    
if __name__ == '__main__':
    #create_data("Belajar argparse")
    #update_data(1)
    #remove_data(1)
    show_data()