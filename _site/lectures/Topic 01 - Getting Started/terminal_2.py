import sys
from time import sleep

adjectives = sys.argv[1]

print("**********************************************")
print("***  Hello to everyone in class today!     ***")
print("**********************************************")

for week, adjective in enumerate(adjectives.split(',')):
    sleep(1)
    print(f"We will learn {adjective} things in Week {(week + 1):02}")