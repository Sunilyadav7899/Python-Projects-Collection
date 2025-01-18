# PROJECT 1: ROCK, PAPER, SCISSOR GAME

"""
1 for rock
0 for paper
-1 for scissor
"""
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
    if(computer == 1 and use == 0):
        print("Congrats, You won!")
    elif(computer == 1 and use == -1):
        print("OOPS, You lost!")
    elif(computer == 0 and use == 1):
        print("OOPS, You lost!")
    elif(computer == 0 and use == -1):
        print("Congrats, You won!")    
    elif(computer == -1 and use == 1):
        print("Congrats, You won!")
    elif(computer == -1 and use == 0):
        print("OOPS, You lost!")
    else:
        print("Something went wrong!")