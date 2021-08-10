from random import Random, randrange
import random

number = random.randint(1,9)
numberOfChances=0
print("Number Guessing Game")
print("You have 5 Chances to guess a number between 1-9 (1 and 9 inclusive)")


while(numberOfChances<5):
    guess= int(input("Enter your guess:- "))
    if (guess>number):
         print("Your guess was too high. Guess a number lower than",guess)
        
    elif (guess<number):
         print("Your guess was too low. Guess a number higher than",guess)
    
    else:
         print("Congratulations you guessed the Correct Number")
    numberOfChances+=1

if (not numberOfChances<5):
    print("YOU LOSE!!! The number is", number)
    

