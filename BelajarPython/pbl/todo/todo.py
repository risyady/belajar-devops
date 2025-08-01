import argparse

parser = argparse.ArgumentParser()

parser.add_argument("add", type=str, help="Menambahkan task")
parser.add_argument("list", help="Menampilkan semua task")
parser.add_argument("done", type=int, help="Menandai task yang sudah selesai")
parser.add_argument("delete", type=int, help="Menghapus task")
args = parser.parse_args()