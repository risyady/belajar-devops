import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="Menampilkan string yang diberikan")
#parser.add_argument("square", help="Memberikan kuadrat dari angka yang diberikan", type=int)

parser.add_argument("x", help="base", type=int)
parser.add_argument("y", help="exponent", type=int)
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="count", default=0)

args = parser.parse_args()
answer = args.x ** args.y

if args.verbose >= 2 :
    print(f"Hasil dari {args.x} dipangkatkan {args.y} adalah {answer}")
elif args.verbose >= 1 :
    print(f"{args.x}^{args.y} = {answer}")
else:
    print(answer)