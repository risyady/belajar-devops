import argparse
import function

parser = argparse.ArgumentParser(description="To Do List CLI")
subparsers = parser.add_subparsers(dest="command")

parser_list = subparsers.add_parser("list", help="Menampilkan semua tugas")

parser_add = subparsers.add_parser("add", help="Menambahkan tugas baru")
parser_add.add_argument("task", type=str, help="Masukkan nama tugas")

parser_done = subparsers.add_parser("done", help="Mengubah status tugas menjadi selesai")
parser_done.add_argument("id_done", type=int, help="Menyelesaikan tugas")

parser_delete = subparsers.add_parser("delete", help="Menghapus tugas")
parser_delete.add_argument("id_delete", type=int, help="Menghapus tugas")

args = parser.parse_args()

args.command = "list" if args.command == None else args.command

match args.command:
    case "list":
        print("List tugas")
        function.show_data()
    case "add":
        print("Menambahkan tugas")
        function.create_data(args.task)
    case "done":
        print(f"Menyelesaikan tugas ID: {args.id_done}")
        function.update_data(args.id_done)
    case "delete":
        print(f"Menghapus tugas ID: {args.id_delete}")
        function.remove_data(args.id_delete)