import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", help="the name of the person you want to find")
parser.add_argument("-a", "--age", help="the age of the person you'd like to find", type=int)
parser.add_argument("-c", "--city", help="the city you'd like to search")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()

if args.verbose:
    print(f"Searching for {args.name} {args.age} years of age in or around {args.city}")
else:
    print(f"Searching for {args.name}")
