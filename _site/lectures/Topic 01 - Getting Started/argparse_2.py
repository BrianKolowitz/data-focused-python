import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("age")
parser.add_argument("city")
args = parser.parse_args()

print(args.name, args.age, args.city)	