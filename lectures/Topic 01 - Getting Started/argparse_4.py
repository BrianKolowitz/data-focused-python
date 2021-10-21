import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="the name of the person you want to find")
parser.add_argument("age", help="the age of the person you'd like to find", type=int)
parser.add_argument("city", help="the city you'd like to search")

args = parser.parse_args()
