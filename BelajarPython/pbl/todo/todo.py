import argparse

parser = argparse.ArgumentParser(description="To Do List CLI")
subparsers = parser.add_subparsers(dest="command")

parser_list = subparsers.add_parser("list", help="Menampilkan semua tugas")

parser_add = subparsers.add_parser("add", help="Menambahkan tugas baru")
parser_add.add_argument("task", type=str, help="Masukkan nama tugas")

parser_done = subparsers.add_parser("done", help="Mengubah status tugas menjadi selesai")
parser_done.add_argument("id", type=int, help="Menyelesaikan tugas")

parser_delete = subparsers.add_parser("delete", help="Menghapus tugas")
parser_delete.add_argument("delete", type=int, help="Menghapus tugas")

args = parser.parse_args()

args.command = "list" if args.command == None else args.command

match args.command:
    case "list":
        print("Fungsi List")
    case "add":
        print("Fungsi Add")
    case "done":
        print("Fungsi Done")
    case "delete":
        print("Fungsi Delete")