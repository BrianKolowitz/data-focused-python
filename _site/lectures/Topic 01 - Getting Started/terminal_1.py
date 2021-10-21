import sys
from time import sleep

adjective = sys.argv[1]
num_weeks = int(sys.argv[2])

print("**********************************************")
print("***  Hello to everyone in class today!     ***")
print("**********************************************")

for week in range(1, num_weeks + 1):
    sleep(1)
    print(f"We will learn {adjective} things in Week {week:02}")