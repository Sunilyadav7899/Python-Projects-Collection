# Guess the number Game.

import random

number = random.randint(1, 100)
a = -1
guesses = 0

while(a != number):
    guesses += 1
    a = int(input("Guess the number :- "))
    if(a > number):
         print(f"“Lower number please”")
    elif(a < number):
        print(f"“higher number please”")

print(f"You have guessed the number ({a} = {number}) correctly in {guesses} attempts ")