# basic flip coin program 
# heads = 1
# tails = 0

import random

computer = random.choice(["head", "tail", "head", "tail"])
users_choice = input("Enter your choice(head or tail): ")


if(computer == users_choice):
    print(f"Congratulations! It's {computer}.")
else:
    print(f"OOPS! It's {computer}.")