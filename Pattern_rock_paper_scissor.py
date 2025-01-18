# rock paper scissor using patterns
import random

computer = random.choice([1, 0, -1])
user = input("Enter your choice(r/p/s): ")
dict = { "r": 1, "p": 0, "s": -1}
reverseDict = {1:"Rock", 0:"Paper", -1:"Scissor"}

use = dict[user]
print(f"You chose '{reverseDict[use]}' \nComputer chose '{reverseDict[computer]}'")


if( computer == use):
    print("Game Draw!")
else:
    if((computer-use) == 2 or (computer-use) == -1):
        print("OOPS, You lost!")
    else:
        print("Congrats, You won!")